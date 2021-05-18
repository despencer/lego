import re
import pandas as pd
import os.path
import logging
from trans import Transform

class Library:
    def __init__(self):
        pass

    @classmethod
    def init(cls):
        logging.basicConfig(filename='ldraw.log', filemode='w', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')
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
        logging.info("Doing " + filename)
        with open(cls.locatefile(filename)) as f:
            lines = f.readlines()
        bounds = Bounds()
        for l in lines:
            l = l.strip()
            if l == '' or l[0] == '0' or l[0] == '5':
                pass
            else:
                values = re.split('[ \t\n]+', l)
                logging.info(values)
                if(values[0] == '1'):
                    trans = Transform.parseldraw(values[2:14])
                    subfile = values[14].replace("\\",os.path.sep)
                    logging.info(trans)
                    if subfile.find('stud') < 0:
                        subbounds = cls.calcbounds(subfile)
                        logging.info("Return to " + filename)
                        subbounds.apply(trans)
                        logging.info("Bounds for %s are %s", subfile, subbounds)
                        bounds.extend(subbounds)
                    else:
                        logging.info('Ignoring %s', subfile)
                elif(values[0] == '2'):
                    bounds.extend(cls.parseldrawpoint(values[2:5]))
                    bounds.extend(cls.parseldrawpoint(values[5:8]))
                elif(values[0] == '3'):
                    bounds.extend(cls.parseldrawpoint(values[2:5]))
                    bounds.extend(cls.parseldrawpoint(values[5:8]))
                    bounds.extend(cls.parseldrawpoint(values[8:11]))
                elif(values[0] == '4'):
                    bounds.extend(cls.parseldrawpoint(values[2:5]))
                    bounds.extend(cls.parseldrawpoint(values[5:8]))
                    bounds.extend(cls.parseldrawpoint(values[8:11]))
                    bounds.extend(cls.parseldrawpoint(values[11:14]))
                else:
                    logging.error("Unknown line type in file {1}: {0}".format(l,filename))
        logging.info("Bounds for {0} are {1}".format(filename, bounds))
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

    @classmethod
    def parseldrawpoint(cls, values):
        res = []
        for i in range(0, 3):
            res.append(Transform.parseldrawvalue(values[i]))
        return res

class Bounds:
    def __init__(self):
        self.min = [ None, None, None, 1 ]
        self.max = [ None, None, None, 1 ]

    def extend(self, point):
        if isinstance(point, Bounds):
            if point.min[0] != None:
                self.extend(point.min)
            if point.max[0] != None:
                self.extend(point.max)
        else:
            for i in range(0, 3):
                self.min[i] = self.minmax(self.min[i], point[i], min)
                self.max[i] = self.minmax(self.max[i], point[i], max)

    def minmax(self, a, b, func):
        if a == None:
            return b
        else:
            return func(a, b)

    def apply(self, trans):
        self.min = self.applypoint(trans, self.min)
        self.max = self.applypoint(trans, self.max)

    def applypoint(self, trans, point):
        if point[0] == None:
            return point
        logging.debug('Point %s', point)
        return trans.applytopoint(point)

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

