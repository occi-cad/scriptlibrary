import cadquery

textoptions = 'something' # set by CQGI

textshape = cadquery.Workplane('top').text(textoptions, fontsize=20, distance=20)

show_object(textshape)