#!/usr/bin/python3

import pandas as pd
import sys

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
        item.position = Transform.id()
        item.file = cls.parts.loc[cls.parts['name'] == name]['part_num'].values[0] + '.dat'
        return item

class Transform:
    def __init__(self):
        pass

    def apply(self, matrix):
        trans = Transform.id()
        for i in range(0, 4):
            for j in range(0, 4):
                trans.matrix[i][j] = 0
                for k in range (0, 4):
                    trans.matrix[i][j] = trans.matrix[i][j] + ( matrix.matrix[i][k] * self.matrix[k][j] )
        return trans

    def copy(self):
        trans = Transform.id()
        for i in range(0, 4):
            for j in range(0, 4):
                trans.matrix[i][j] = self.matrix[i][j]
        return trans

    def reprldraw(self):
        z = [ ]
        for i in range(0, 3):
            z.append(self.matrix[i][3])
        for i in range(0, 3):
            z.extend(self.matrix[i][0:3])
        return ' '.join(str(d) for d in z)

    @classmethod
    def id(cls):
        trans = cls()
        trans.matrix = [ [ 1, 0, 0, 0 ], [ 0, 1, 0, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 0, 1] ]
        return trans

    @classmethod
    def translation(cls, x, y, z):
        trans = cls.id()
        trans.matrix[0][3] = x
        trans.matrix[1][3] = y
        trans.matrix[2][3] = z
        return trans

    @classmethod
    def swapyz(cls):
        trans = cls()
        trans.matrix = [ [ 1, 0, 0, 0 ],
                         [ 0, 0, 1, 0 ],
                         [ 0, 1, 0, 0 ],
                         [ 0, 0, 0, 1] ]
        return trans

class Item:
    def __init__(self):
        pass

    def transform(self, matrix):
        self.position = self.position.apply(matrix)

    def emitldraw(self, stream, ldtrans):
        stream.write("1 {0} {1} {2}\r\n".format(self.color, self.position.copy().apply(ldtrans).reprldraw(), self.file ) )

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

    def emitldraw(self, stream, ldtrans = None):
        if ldtrans == None:
            ldtrans = Transform.id()
        for x in self.items:
            x.emitldraw(stream, ldtrans = ldtrans)

def createrow(color, sizex, sizey):
    model = Compound()
    for x in range(0, sizex):
        model.addbrick('Brick 1 x 4', x*4, 0, 0, color=2)
        model.addbrick('Brick 1 x 4', x*4+1, sizey*4, 0, color=4)
    return model

Library.init()
model = createrow(2, 5, 2)
model.emitldraw(sys.stdout)