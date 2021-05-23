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

    def applytopoint(self, point):
        res = [ 0, 0, 0, 0 ]
        for i in range(0, 4):
            for j in range(0, 4):
                res[i] = res[i] + ( self.matrix[i][j] * point[j] )
        return res

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
    def parseldraw(cls, pres):
        if len(pres) != 12:
           raise ValueError
        trans = Transform.id()
        for i in range(0, 3):
            trans.matrix[i][3] = cls.parseldrawvalue(pres[i])
        for i in range(0, 3):
            for j in range(0, 3):
                trans.matrix[i][j] = cls.parseldrawvalue(pres[3*(i+1)+j])
        return trans

    @classmethod
    def parseldrawvalue(cls, value):
        return float(value) if '.' in value else int(value)

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
    def translationp(cls, point):
        return cls.translation(point[0], point[1], point[2])

    @classmethod
    def swapyz(cls):
        trans = cls()
        trans.matrix = [ [ 1, 0, 0, 0 ],
                         [ 0, 0, 1, 0 ],
                         [ 0, 1, 0, 0 ],
                         [ 0, 0, 0, 1] ]
        return trans

    @classmethod
    def rotatexy(cls):
        trans = cls()
        trans.matrix = [ [ 0, 1, 0, 0 ],
                         [ -1, 0, 0, 0 ],
                         [ 0, 0, 1, 0 ],
                         [ 0, 0, 0, 1] ]
        return trans

    @classmethod
    def flipy(cls):
        trans = cls()
        trans.matrix = [ [ 1, 0, 0, 0 ],
                         [ 0, -1, 0, 0 ],
                         [ 0, 0, 1, 0 ],
                         [ 0, 0, 0, 1] ]
        return trans

    @classmethod
    def toldraw(cls):
        return cls.id().apply(cls.swapyz()).apply(cls.flipy())

    @classmethod
    def fromldraw(cls):
        return cls.id().apply(cls.flipy()).apply(cls.swapyz())

    def __repr__(self):
        return str(self.matrix)