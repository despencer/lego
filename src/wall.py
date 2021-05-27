#!/usr/bin/python3

import sys
from trans import Transform
from ldraw import Library, Item, Compound

def createrow(model, color, sizex, sizey, z):
    if model == None:
        model = Compound()
    xy = Transform.rotatexy()
    for x in range(0, sizex):
        model.addbrick('Brick 1 x 4', x*4, 0, z, color)
        model.addbrick('Brick 1 x 4', x*4+1, sizey*4, z, color)
    for y in range(0, sizey):
        model.addbrick('Brick 1 x 4', 0, y*4+1, z, color, rotation=xy)
        model.addbrick('Brick 1 x 4', sizex*4, y*4, z, color, rotation=xy)
    return model

Library.init()
model = createrow(None, 'White', 2, 2, 0)
createrow(model, 'Trans-Clear', 2, 2, 1)
createrow(model, 'Black', 2, 2, 2)
createrow(model, 'lbg', 2, 2, 3)
model.emitldraw(sys.stdout)