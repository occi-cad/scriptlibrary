// Archiyou 0.1
// units in mm

WIDTH = $WIDTH;
HEIGHT = $HEIGHT;
DEPTH = $DEPTH;
THICKNESS = $THICKNESS;
FILLET_RADIUS = 10;
HOLE_FROM_END = 15;
HOLE_DIAM = $HOLE_DIAM;
HOLE_CHAMFER = 0.6; // percent of THICKNESS 

vert = box(THICKNESS,WIDTH,HEIGHT)
        .move(THICKNESS/2,0,HEIGHT/2);
hor = box(DEPTH, WIDTH, THICKNESS)
        .move(DEPTH/2, 0, THICKNESS/2)

bracket = vert.unioned(hor).color('blue');
vert.hide();
hor.hide();
bracket.fillet(10,'E[17]');

subHoleHor = cylinder(HOLE_DIAM/2)
            .move(DEPTH-HOLE_FROM_END);
subHoleVert = cylinder(HOLE_DIAM/2)
            .rotateY(90)
            .move(0,0,HEIGHT-HOLE_FROM_END);

bracket.subtract([subHoleHor.hide()
                    ,subHoleVert.hide()]);

bracket.chamfer(HOLE_CHAMFER*THICKNESS,'E[10,15]')