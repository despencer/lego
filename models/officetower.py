#!/usr/bin/python3

import sys
import os

sys.path.append(os.path.abspath('../src'))
from trans import Transform
from ldraw import Library, Item, Compound

def createmainrow(row):
    model = Compound("Row{0}".format(row))
    xy = Transform.rotatexy()
    model.addbrick('Brick 1 x 4', 0, 2, 0, color='White')
    model.addbrick('Brick 1 x 2', 0, 3, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 2', 0, 5, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 2', 0, 7, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 3', 0, 9, 0, color='White')
    model.addbrick('Brick 1 x 2', 2, 10, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 2', 3, 11, 0, color='Trans-Light Blue')
    model.addbrick('Brick 1 x 2', 2, 0, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 2', 3, 0, 0, color='Trans-Light Blue')
    for i in range (0, 4):
        model.addbrick('Brick 1 x 4', 5+i*4, 8, 0, color='White', rotation=xy)
        model.addbrick('Brick 1 x 2', 6+i*4, 10, 0, color='Trans-Light Blue', rotation=xy)
        model.addbrick('Brick 1 x 2', 7+i*4, 10, 0, color='Trans-Light Blue', rotation=xy)
        model.addbrick('Brick 1 x 2', 8+i*4, 10, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 4', 21, 8, 0, color='White', rotation=xy)
    model.addbrick('Brick 1 x 2', 22, 11, 0, color='Trans-Light Blue')
    model.addbrick('Brick 1 x 2', 24, 10, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 3', 22, 9, 0, color='White')
    for i in range (0, 4):
        model.addbrick('Brick 1 x 4', 5+i*4, 0, 0, color='White', rotation=xy)
        model.addbrick('Brick 1 x 2', 6+i*4, 0, 0, color='Trans-Light Blue', rotation=xy)
        model.addbrick('Brick 1 x 2', 7+i*4, 0, 0, color='Trans-Light Blue', rotation=xy)
        model.addbrick('Brick 1 x 2', 8+i*4, 0, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 4', 21, 0, 0, color='White', rotation=xy)
    model.addbrick('Brick 1 x 2', 22, 0, 0, color='Trans-Light Blue')
    model.addbrick('Brick 1 x 2', 24, 0, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 3', 22, 2, 0, color='White')
    model.addbrick('Brick 1 x 2', 24, 3, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 2', 24, 5, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 2', 24, 7, 0, color='Trans-Light Blue', rotation=xy)
    return model

Library.init()
mainrow = createmainrow(0)
mainrow.emitldraw(sys.stdout, Transform.translation(0, 0, 24))
