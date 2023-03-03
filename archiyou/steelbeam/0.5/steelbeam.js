flangeBottom = rect($WIDTH,$FLANGE_THICKNESS).move(0,$HEIGHT/2-$FLANGE_THICKNESS/2);
flangeTop = rect($WIDTH,$FLANGE_THICKNESS).move(0,-$HEIGHT/2+$FLANGE_THICKNESS/2);
web = rect($WEB_THICKNESS,$HEIGHT);
profile = web.unioned(flangeBottom).union(flangeTop).color('red');

flangeTop.hide();
flangeBottom.hide();
web.hide();

profile.fillet(5, 'V[8,9,2,3]')
profile.extrude($LENGTH*10); // LENGTH in cm