import cadquery
import time

size = 50

box=cadquery.Workplane('top').box(size,size,size)
time.sleep(10)

show_object(box)