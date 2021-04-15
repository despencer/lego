import pandas as pd
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

    @classmethod
    def rotatexy(cls, item):
        item.transform(Transform.rotatexy())

    def emitldraw(self, stream):
        stream.write("1 {0} {1} {2}\r\n".format(self.color, self.position.apply(Transform.toldraw()).reprldraw(), self.file ) )

    @classmethod
    def frombrick(cls, name, x, y, z, color=15, rotation=None):
        item = Library.getbyname(name)
        item.color = color
        if rotation != None:
            rotation(item)
        item.transform(Transform.translation( x*20, y*20, z*24 ) )
        return item

class Compound:
    def __init__(self):
        self.items = []

    def addbrick(self, name, x, y, z, color=15, rotation=None):
        item = Item.frombrick(name, x, y, z, color, rotation)
        self.items.append(item)
        return item

    def emitldraw(self, stream):
        for x in self.items:
            x.emitldraw(stream)

