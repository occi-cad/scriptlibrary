import cadquery
from cq_warehouse.fastener import HexNut

# PARAMS
SIZE='M3-0.5'
TYPE='iso4032'
HAND='right'

nut = HexNut(size=SIZE, fastener_type=TYPE, hand=HAND)

show_object(nut)

