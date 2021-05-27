#!/usr/bin/python3

import sys
from trans import Transform
from ldraw import Library, Item, Compound

def createrow(model, color, sizex, sizey, z):
    if model == None:
        model = Compound()
    xy = Transform.rotatexy()
    for x in range(0, sizex):
        model.addbrick('Brick 1 x 4', x*4, 0, z, color=2)
        model.addbrick('Brick 1 x 4', x*4+1, sizey*4, z, color=3)
    for y in range(0, sizey):
        model.addbrick('Brick 1 x 4', 0, y*4+1, z, color=4, rotation=xy)
        model.addbrick('Brick 1 x 4', sizex*4, y*4, z, color=5, rotation=xy)
    return model

Library.init()
model = createrow(None, 2, 2, 2, 0)
createrow(model, 2, 2, 2, 1)
model.emitldraw(sys.stdout)