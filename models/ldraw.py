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
        logging.basicConfig(filename='ldraw.log', filemode='w', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')
        cls.parts = pd.read_csv('/usr/share/rebrickable/parts.csv')
        cls.bounds = dict()

    @classmethod
    def getbyname(cls, name):
        item = Item()
        item.color = 15
        item.file = cls.parts.loc[cls.parts['name'] == name]['part_num'].values[0] + '.dat'
        item.position = cls.getposition(item.file)
        return item

    @classmethod
    def getposition(cls, filename):
        if filename not in cls.bounds:
            bounds = cls.calcbounds(filename)
            cls.bounds[filename] = bounds.gettranslation().apply(Transform.fromldraw())
            logging.debug("For %s transforming with %s", filename, Transform.fromldraw())
            logging.info('For %s default position set %s', filename, cls.bounds[filename])
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

    def gettranslation(self):
        if self.min[0] == None:
            return Transform.id()
        else:
            return Transform.translation(-self.min[0], -self.min[1], -self.min[2])

    def __repr__(self):
        return "[ {0} - {1} ]".format(self.min, self.max)

class Item:
    def __init__(self):
        pass

    def transform(self, matrix):
        logging.debug("Item %s is about to be transformed with %s", self.file, matrix)
        self.position = self.position.apply(matrix)

    @classmethod
    def rotatexy(cls, item):
        item.transform(Transform.rotatexy())

    def emitldraw(self, stream):
        logging.debug("Emit %s from %s", self.file, self.position)
        logging.debug("Emit %s with %s to %s", self.file, Transform.toldraw(), self.position.apply(Transform.toldraw()))
        stream.write("1 {0} {1} {2}\r\n".format(self.color, self.position.apply(Transform.toldraw()).reprldraw(), self.file ) )

    @classmethod
    def frombrick(cls, name, x, y, z, color=15, rotation=None):
        logging.debug("Item %s at (%s,%s,%s)",name,x,y,z)
        item = Library.getbyname(name)
        item.color = color
        logging.debug("Item %s at %s",name, item.position)
        if rotation != None:
            rotation(item)
        item.transform(Transform.translation( x*20, y*20, z*24 ) )
        logging.debug("Item %s finally at %s",name, item.position)
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

