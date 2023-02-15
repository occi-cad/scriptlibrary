import cadquery as cq
from cq_warehouse.fastener import HexNut, SocketHeadCapScrew, SetScrew

# Parameters
fastener_type = "screw"
head_type = "set"
fastener_size = "M3-0.5"
fastener_length = 10

# Figure out what type of fastener the user requested
if fastener_type == "nut":
    fastener = HexNut(size=fastener_size, fastener_type="iso4032")
elif fastener_type == "screw":
    if head_type == "set":
        fastener = SetScrew(size=fastener_size, fastener_type="iso4026",length=fastener_length)
    if head_type == "socket head":
        fastener = SocketHeadCapScrew(size=fastener_size, fastener_type="iso4762", length=fastener_length)

show_object(fastener)
