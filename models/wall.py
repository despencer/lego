#!/usr/bin/python3

import pandas as pd
import sys
from trans import Transform

class Library:
    def __init__(self):
        pass

    @classmethod
    def init(cls):
        cls.parts = pd.read_csv('/usr/share/rebrickable/parts.csv')

    @classmethod
    def getbyname(cls, name):
        item = Item()
        item.color = 15
        item.position = Transform.fromldraw()
        item.file = cls.parts.loc[cls.parts['name'] == name]['part_num'].values[0] + '.dat'
        return item

class Item:
    def __init__(self):
        pass

    def transform(self, matrix):
        self.position = self.position.apply(matrix)

    def emitldraw(self, stream):
        stream.write("1 {0} {1} {2}\r\n".format(self.color, self.position.apply(Transform.toldraw()).reprldraw(), self.file ) )

    @classmethod
    def frombrick(cls, name, x, y, z, color=15):
        item = Library.getbyname(name)
        item.color = color
        item.transform(Transform.translation( x*20, y*20, z*24 ) )
        return item

class Compound:
    def __init__(self):
        self.items = []

    def addbrick(self, name, x, y, z, color=15):
        self.items.append(Item.frombrick(name, x, y, z, color))

    def emitldraw(self, stream):
        for x in self.items:
            x.emitldraw(stream)

def createrow(color, sizex, sizey):
    model = Compound()
    for x in range(0, sizex):
        model.addbrick('Brick 1 x 4', x*4, 0, 0, color=2)
        model.addbrick('Brick 1 x 4', x*4+1, sizey*4, 0, color=4)
    return model

Library.init()
model = createrow(2, 5, 2)
model.emitldraw(sys.stdout)