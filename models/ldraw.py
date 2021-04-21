import re
import pandas as pd
import os.path
from trans import Transform

class Library:
    def __init__(self):
        pass

    @classmethod
    def init(cls):
        cls.parts = pd.read_csv('/usr/share/rebrickable/parts.csv')
        cls.bounds = dict()

    @classmethod
    def getbyname(cls, name):
        item = Item()
        item.color = 15
        item.file = cls.parts.loc[cls.parts['name'] == name]['part_num'].values[0] + '.dat'
        Library.getbounds(item.file)
        item.position = Transform.fromldraw()
        return item

    @classmethod
    def getbounds(cls, filename):
        if filename not in cls.bounds:
            cls.bounds[filename] = cls.calcbounds(filename)
        return cls.bounds[filename]

    @classmethod
    def calcbounds(cls, filename):
        print("Doing " + filename)
        with open(cls.locatefile(filename)) as f:
            lines = f.readlines()
        bounds = Bounds()
        for l in lines:
            l = l.strip()
            if l == '' or l[0] == '0':
                pass
            else:
                values = re.split('[ \t\n]+', l)
                print(values)
                if(values[0] == '1'):
                    trans = Transform.parseldraw(values[2:14])
                    subfile = values[14].replace("\\",os.path.sep)
                    print(trans)
                    subbounds = cls.calcbounds(subfile)
                elif(values[0] == '2'):
                    bounds.extend(values[2:5])
                    bounds.extend(values[5:8])
                elif(values[0] == '3'):
                    bounds.extend(values[2:5])
                    bounds.extend(values[5:8])
                    bounds.extend(values[8:11])
                elif(values[0] == '4'):
                    bounds.extend(values[2:5])
                    bounds.extend(values[5:8])
                    bounds.extend(values[8:11])
                    bounds.extend(values[11:14])
                else:
                    print("Unknown line type in file {1}: {0}".format(l,filename))
        print("Bounds for {0} are {1}".format(filename, bounds))
        return bounds

    @classmethod
    def locatefile(cls, filename):
        file = "/usr/share/ldraw/parts/"+filename
        if os.path.isfile(file):
            return file
        file = "/usr/share/ldraw/p/"+filename
        if os.path.isfile(file):
            return file
        raise FileNotFoundError

class Bounds:
    def __init__(self):
        self.min = [ None, None, None, 1 ]
        self.max = [ None, None, None, 1 ]

    def extend(self, point):
        for i in range(0, 3):
            self.min[i] = self.minmax(self.min[i], point[i], min)
            self.max[i] = self.minmax(self.max[i], point[i], max)

    def minmax(self, a, b, func):
        if a == None:
            return b
        else:
            return func(a, b)

    def __repr__(self):
        return "[ {0} - {1} ]".format(self.min, self.max)

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

