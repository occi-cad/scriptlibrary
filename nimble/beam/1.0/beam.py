import cadquery as cq

# Parameters
length = 294  # mm
hole_spacing = 14  # mm
long_axis_hole_dia = 4.6  # mm
mounting_holes_dia = 3.6  # mm

# Create the outside profile
beam = cq.Workplane().rect(20, 20).extrude(length)

# Outside rounds
beam = beam.edges("|Z").fillet(2.0)

# Channel cutouts
pl = cq.Workplane().polyline([(-2.5, -1.5), (-5, 1.5), (5, 1.5), (2.5, -1.5)]).close().rotateAboutCenter((0, 0, 1), -90).val()
beam = (beam.faces("<Z")
            .polarArray(10, 0, 360, 4, rotate=True)
            .eachpoint(lambda loc: pl.moved(loc))
            .cutThruAll())

# Center hole
beam = beam.faces("<Z").workplane().hole(long_axis_hole_dia)

# Mounting holes
beam = beam.faces("<Y").workplane().center(0, length / 2.0).rarray(1, 14.0, 1, 21).hole(mounting_holes_dia)
beam = beam.faces("<X").workplane().center(-10, 0).rarray(1, hole_spacing, 1, 21).hole(mounting_holes_dia)

# Uncomment to export STL
# cq.exporters.export(beam, "/home/jwright/Downloads/beam_test.stl")

show_object(beam)