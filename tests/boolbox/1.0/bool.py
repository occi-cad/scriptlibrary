import cadquery

isbig = True # gets set by CQGI
size = 100 if isbig else 10

box=cadquery.Workplane('top').box(size,size,size)

show_object(box)