import cadquery

text = "parametric text"

textshape = cadquery.Workplane('top').text(text, fontsize=20, distance=20)

show_object(textshape)