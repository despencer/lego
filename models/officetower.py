#!/usr/bin/python3

import sys
import os

sys.path.append(os.path.abspath('../src'))
from trans import Transform
from ldraw import Library, Item, Compound

xy = Transform.rotatexy()
xy3 = Transform.rotatexy3()
mode = "prod"
floors = 12

def createmainrow(row):
    model = Compound("Row{0}".format(row))
    model.addbrick('Brick 1 x 4', 0, 2, 0, color='White')
    model.addbrick('Brick 1 x 2', 0, 3, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 2', 0, 5, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 2', 0, 7, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 4', 0, 9, 0, color='White')
    model.addbrick('Brick 1 x 2', 2, 10, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 2', 3, 11, 0, color='Trans-Light Blue')
    model.addbrick('Brick 1 x 2', 2, 0, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 2', 3, 0, 0, color='Trans-Light Blue')
    for i in range (0, 4):
        model.addbrick('Brick 1 x 2', 6+i*4, 10, 0, color='Trans-Light Blue', rotation=xy)
        model.addbrick('Brick 1 x 2', 7+i*4, 10, 0, color='Trans-Light Blue', rotation=xy)
        model.addbrick('Brick 1 x 2', 8+i*4, 10, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 2', 22, 11, 0, color='Trans-Light Blue')
    model.addbrick('Brick 1 x 2', 24, 10, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 3', 22, 9, 0, color='White')
    for i in range (0, 4):
        model.addbrick('Brick 1 x 12', 5+i*4, 0, 0, color='White', rotation=xy)
        model.addbrick('Brick 1 x 2', 6+i*4, 0, 0, color='Trans-Light Blue', rotation=xy)
        model.addbrick('Brick 1 x 2', 7+i*4, 0, 0, color='Trans-Light Blue', rotation=xy)
        model.addbrick('Brick 1 x 2', 8+i*4, 0, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 12', 21, 0, 0, color='White', rotation=xy)
    model.addbrick('Brick 1 x 2', 22, 0, 0, color='Trans-Light Blue')
    model.addbrick('Brick 1 x 2', 24, 0, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 3', 22, 2, 0, color='White')
    model.addbrick('Brick 1 x 2', 24, 3, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 2', 24, 5, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 2', 24, 7, 0, color='Trans-Light Blue', rotation=xy)
    return model

def createinterimrow1(row):
    model = Compound("Interim1.{0}".format(row))
    model.addbrick('Plate 1 x 4', 0, 2, 0, color='White')
    model.addbrick('Plate 1 x 2', 0, 3, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Plate 1 x 2', 0, 5, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Plate 1 x 2', 0, 7, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Plate 1 x 4', 0, 9, 0, color='White')
    model.addbrick('Plate 2 x 10', 2, 0, 0, color='White' if mode == 'prod' else 'Black')
    model.addbrick('Plate 2 x 3', 12, 0, 0, color='White')
    model.addbrick('Plate 2 x 10',15, 0, 0, color='White' if mode == 'prod' else 'Black')
    model.addbrick('Plate 2 x 10', 2, 10, 0, color='White' if mode == 'prod' else 'Black')
    model.addbrick('Plate 2 x 3', 12, 10, 0, color='White')
    model.addbrick('Plate 2 x 10',15, 10, 0, color='White' if mode == 'prod' else 'Black')
    model.addbrick('Plate 1 x 4', 21, 2, 0, color='White')
    model.addbrick('Plate 1 x 2', 24, 3, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Plate 1 x 2', 24, 5, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Plate 1 x 2', 24, 7, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Plate 1 x 4', 21, 9, 0, color='White')
    return model

def createinterimrow2(row):
    model = Compound("Interim2.{0}".format(row))
    model.addbrick('Plate 2 x 8', 0, 2, 0, color='White', rotation=xy)
    model.addbrick('Plate 2 x 12', 2, 0, 0, color='White' if mode == 'prod' else 'Black', rotation=xy)
    model.addbrick('Plate 2 x 10', 4, 0, 0, color='White')
    model.addbrick('Plate 1 x 12', 14, 0, 0, color='White' if mode == 'prod' else 'Black', rotation=xy)
    model.addbrick('Plate 2 x 8', 15, 0, 0, color='White')
    model.addbrick('Plate 2 x 10', 4, 10, 0, color='White')
    model.addbrick('Plate 2 x 8', 15, 10, 0, color='White')
    model.addbrick('Plate 2 x 12', 23, 0, 0, color='White' if mode == 'prod' else 'Black', rotation=xy)
    return model

def createinterimrow3(row):
    model = Compound("Interim3.{0}".format(row))
    model.addbrick('Plate 1 x 2', 0, 2, 0, color='White')
    model.addbrick('Plate 1 x 2', 0, 3, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Plate 1 x 2', 0, 5, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Plate 1 x 2', 0, 7, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Plate 1 x 2', 0, 9, 0, color='White')
    model.addbrick('Plate 2 x 10', 2, 0, 0, color='White' if mode == 'prod' else 'Black')
    model.addbrick('Plate 2 x 10', 2, 2, 0, color='White' if mode == 'prod' else 'Green')
    model.addbrick('Plate 2 x 3', 12, 0, 0, color='White')
    model.addbrick('Plate 2 x 3', 12, 2, 0, color='White' if mode == 'prod' else 'Yellow')
    model.addbrick('Plate 2 x 10',15, 0, 0, color='White' if mode == 'prod' else 'Black')
    model.addbrick('Plate 2 x 8',15, 2, 0, color='White' if mode == 'prod' else 'Green')
    model.addbrick('Plate 2 x 10', 2, 10, 0, color='White' if mode == 'prod' else 'Black')
    model.addbrick('Plate 2 x 10', 2, 8, 0, color='White' if mode == 'prod' else 'Green')
    model.addbrick('Plate 2 x 3', 12, 10, 0, color='White')
    model.addbrick('Plate 2 x 3', 12, 8, 0, color='White' if mode == 'prod' else 'Yellow')
    model.addbrick('Plate 2 x 10',15, 10, 0, color='White' if mode == 'prod' else 'Black')
    model.addbrick('Plate 2 x 8',15, 8, 0, color='White' if mode == 'prod' else 'Green')
    model.addbrick('Plate 1 x 2', 23, 2, 0, color='White')
    model.addbrick('Plate 1 x 2', 24, 3, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Plate 1 x 2', 24, 5, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Plate 1 x 2', 24, 7, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Plate 1 x 2', 23, 9, 0, color='White')
    return model

def createinterimrow4(row):
    model = Compound("Interim2.{0}".format(row))
    model.addbrick('Plate 2 x 8', 0, 2, 0, color='White', rotation=xy)
    model.addbrick('Plate 2 x 8', 2, 2, 0, color='White' if mode == 'prod' else 'Black', rotation=xy)
    model.addbrick('Plate 2 x 10', 4, 2, 0, color='White')
    model.addbrick('Plate 1 x 8', 14, 2, 0, color='White' if mode == 'prod' else 'Black', rotation=xy)
    model.addbrick('Plate 2 x 8', 15, 2, 0, color='White')
    model.addbrick('Plate 2 x 10', 4, 8, 0, color='White')
    model.addbrick('Plate 2 x 8', 15, 8, 0, color='White')
    model.addbrick('Plate 2 x 8', 23, 2, 0, color='White' if mode == 'prod' else 'Black', rotation=xy)
    for i in range(0, 11):
        model.addbrick('Tile 2 x 2 with Groove', 2+2*i, 0, 0, color='White' if mode == 'prod' else ('Red' if i%2==0 else 'Blue'))
        model.addbrick('Tile 2 x 2 with Groove', 2+2*i, 10, 0, color='White' if mode == 'prod' else ('Red' if i%2==0 else 'Blue'))
    model.addbrick('Tile 1 x 2 with Groove', 24, 0, 0, color='White' if mode == 'prod' else 'Green', rotation=xy)
    model.addbrick('Tile 1 x 2 with Groove', 24, 10, 0, color='White' if mode == 'prod' else 'Green', rotation=xy)
    return model

def createtoprow1():
    model = Compound("TopRow1")
    model.addbrick('Brick 1 x 2', 0, 2, 0, color='White')
    model.addbrick('Brick 1 x 2', 0, 3, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 2', 0, 5, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 2', 0, 7, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 2', 0, 9, 0, color='White')
    for i in range(0, 5):
        for j in range(0, 6):
            model.addbrick('Brick 1 x 2', 2+i*4+int(j/2), 2+6*(j%2), 0, color='Trans-Light Blue', rotation=xy)
        model.addbrick('Brick 1 x 8', 5+i*4, 2, 0, color='White', rotation=xy)
    model.addbrick('Brick 1 x 2', 22, 2, 0, color='Trans-Light Blue')
    model.addbrick('Brick 1 x 1', 24, 2, 0, color='White')
    model.addbrick('Brick 1 x 2', 24, 3, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 2', 24, 5, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 2', 24, 7, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Brick 1 x 2', 22, 9, 0, color='Trans-Light Blue')
    model.addbrick('Brick 1 x 1', 24, 9, 0, color='White')
    return model

def createtoprow2():
    model = Compound("TopRow2")
    model.addbrick('Plate 1 x 2', 0, 3, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Plate 1 x 2', 0, 5, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Plate 1 x 2', 0, 7, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Plate 1 x 6', 0, 3*20, 8, color='White' if mode == 'prod' else 'Yellow', rotation=xy, brickunits=False)
    model.addbrick('Plate 1 x 6', 0, 3*20, 16, color='White', rotation=xy, brickunits=False)
    for i in range(0, 3):
        model.addbrick('Brick 1 x 6', i*6, 2, 0, color='White' if mode == 'prod' else ('Red' if i%2==0 else 'Blue'))
        model.addbrick('Brick 1 x 6', i*6, 9, 0, color='White' if mode == 'prod' else ('Red' if i%2==0 else 'Blue'))
        model.addbrick('Brick 1 x 6', 1+i*6, 3, 0, color='White' if mode == 'prod' else ('Yellow' if i%2==0 else 'Green'))
        model.addbrick('Brick 1 x 6', 1+i*6, 8, 0, color='White' if mode == 'prod' else ('Yellow' if i%2==0 else 'Green'))
    model.addbrick('Brick 1 x 4', 18, 2, 0, color='White' if mode == 'prod' else 'Blue')
    model.addbrick('Brick 1 x 4', 18, 9, 0, color='White' if mode == 'prod' else 'Blue')
    model.addbrick('Brick 1 x 3', 22, 2, 0, color='White' if mode == 'prod' else 'Red')
    model.addbrick('Brick 1 x 3', 22, 9, 0, color='White' if mode == 'prod' else 'Red')
    model.addbrick('Brick 1 x 4', 19, 3, 0, color='White' if mode == 'prod' else 'Green')
    model.addbrick('Brick 1 x 4', 19, 8, 0, color='White' if mode == 'prod' else 'Green')
    model.addbrick('Plate 1 x 2', 24, 3, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Plate 1 x 2', 24, 5, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Plate 1 x 2', 24, 7, 0, color='Trans-Light Blue', rotation=xy)
    model.addbrick('Plate 1 x 6', 24*20, 3*20, 8, color='White' if mode == 'prod' else 'Yellow', rotation=xy, brickunits=False)
    model.addbrick('Plate 1 x 6', 24*20, 3*20, 16, color='White', rotation=xy, brickunits=False)
    return model

def createroofrow1():
    model = Compound("RoofRow1")
    model.addbrick('88930', 0, 2, 0, color='White' if mode == 'prod' else 'Yellow', rotation=xy3)
    model.addbrick('88930', 0, 6, 0, color='White' if mode == 'prod' else 'Green', rotation=xy3)
    model.addbrick('Plate 1 x 8', 2, 2, 0, color='White' if mode == 'prod' else 'Blue', rotation=xy)
    for i in range (0, 10):
        model.addbrick('Plate 2 x 8', 3+i*2, 2, 0, color='White' if mode == 'prod' else ('Red' if i%2==0 else 'Blue'), rotation=xy)
    model.addbrick('88930', 23, 2, 0, color='White' if mode == 'prod' else 'Yellow', rotation=xy)
    model.addbrick('88930', 23, 6, 0, color='White' if mode == 'prod' else 'Green', rotation=xy)
    return model

Library.init()

mode = 'dev'

model = Compound("Office Tower")
if mode == 'dev':
    model.add(createmainrow(0)).transform(Transform.translation(0, 0, 24))
    model.add(createinterimrow1(0)).transform(Transform.translation(0, 0, 72))
    model.add(createinterimrow2(0)).transform(Transform.translation(0, 0, 144))
    model.add(createmainrow(0)).transform(Transform.translation(0, 0, 216))
    model.add(createinterimrow3(0)).transform(Transform.translation(0, 0, 288))
    model.add(createinterimrow4(0)).transform(Transform.translation(0, 0, 360))
else:
    model.add(createmainrow(-1)).transform(Transform.translation(0, 0, 24))
    for i in range (0, floors if mode == 'prod' else 1):
        model.add(createmainrow(i)).transform(Transform.translation(0, 0, 48 + i*40))
        if i < floors-1:
            model.add(createinterimrow1(i)).transform(Transform.translation(0, 0, 72 + i*40))
            model.add(createinterimrow2(i)).transform(Transform.translation(0, 0, 80 + i*40))
        else:
            model.add(createinterimrow3(i)).transform(Transform.translation(0, 0, 72 + i*40))
            model.add(createinterimrow4(i)).transform(Transform.translation(0, 0, 80 + i*40))

model.add(createtoprow1()).transform(Transform.translation(0, 0, (48 + floors*40) if mode == 'prod' else 408))
model.add(createtoprow2()).transform(Transform.translation(0, 0, (72 + floors*40) if mode == 'prod' else 456))
model.add(createroofrow1()).transform(Transform.translation(0, 0, (96 + floors*40) if mode == 'prod' else 504))

model.emitldraw(sys.stdout, Transform.id())
