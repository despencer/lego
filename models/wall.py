#!/usr/bin/python3

import sys
from trans import Transform
from ldraw import Library, Item, Compound

def createrow(color, sizex, sizey):
    model = Compound()
    for x in range(0, sizex):
        model.addbrick('Brick 1 x 4', x*4, 0, 0, color=2)
        model.addbrick('Brick 1 x 4', x*4+1, sizey*4, 0, color=3)
    for y in range(0, sizey):
        model.addbrick('Brick 1 x 4', 0, y*4+1, 0, color=4, rotation=Item.rotatexy)
        model.addbrick('Brick 1 x 4', sizex*4, y*4, 0, color=5, rotation=Item.rotatexy)
    return model

Library.init()
model = createrow(2, 5, 2)
model.emitldraw(sys.stdout)