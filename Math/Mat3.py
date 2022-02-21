"""
Simple Mat3 class which can be used with the Vec3 class
"""

import copy
import functools
import math
import operator

from Math.Vec3 import Vec3


class Mat3Error(Exception):
    """An exception class for Mat3"""

    pass


class Mat3NotSquare(Exception):
    """Make sure we have 3x3"""

    pass


class Mat3:
    __slots__ = ["m"]

    def __init__(self):
        self.m = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]

    def get_matrix(self):
        "return matrix as list"
        return functools.reduce(operator.concat, self.m)

    @classmethod
    def identity(cls):
        "class method to return a new identity matrix"
        v = Mat3()
        return v

    @classmethod
    def zero(cls):
        "class method to return a zero matrix"
        v = Mat3()
        v.m = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
        return v

    @classmethod
    def from_list(cls, l):
        "class method to create mat3 from list"
        v = Mat3()
        v.m = l
        if v._is_square() is not True:
            raise Mat3NotSquare
        else:
            return v

    def _is_square(self) -> bool:
        "ensure matrix is square"
        return len(self.m) == 3 and all(len(i) == 3 for i in self.m)

    def transpose(self):
        "traspose this matrix"
        self.m = [list(item) for item in zip(*self.m)]

    def get_transpose(self):
        "return a new matrix as the transpose of ourself"
        m = Mat3()
        m.m = [list(item) for item in zip(*self.m)]
        return m

    def _identity(self):
        "set this matrix to identity"
        self.m = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]

    def scale(self, x: float, y: float, z: float):
        "set this matrix to be a scale matrix resetting to identity first"
        self._identity()
        self.m[0][0] = x
        self.m[1][1] = y
        self.m[2][2] = z

    def rotateX(self, angle: float):
        "set this matrix to be a rotation around the X axis by angle degrees"
        self._identity()
        beta = math.radians(angle)
        sr = math.sin(beta)
        cr = math.cos(beta)
        self.m[1][1] = cr
        self.m[1][2] = sr
        self.m[2][1] = -sr
        self.m[2][2] = cr

    def rotateY(self, angle: float):
        "set this matrix to be a rotation around the y axis by angle degrees"
        self._identity()
        beta = math.radians(angle)
        sr = math.sin(beta)
        cr = math.cos(beta)
        self.m[0][0] = cr
        self.m[0][2] = -sr
        self.m[2][0] = sr
        self.m[2][2] = cr

    def rotateZ(self, angle: float):
        "set this matrix to be a rotation around the Z axis by angle degrees"
        self._identity()
        beta = math.radians(angle)
        sr = math.sin(beta)
        cr = math.cos(beta)
        self.m[0][0] = cr
        self.m[0][1] = sr
        self.m[1][0] = -sr
        self.m[1][1] = cr

    def __getitem__(self, idx):
        return self.m[idx]

    def __setitem__(self, idx, item):
        self.m[idx] = item

    def __mul__(self, rhs):
        mat_t = rhs.get_transpose()
        mulmat = Mat3()
        for x in range(3):
            for y in range(3):
                mulmat[x][y] = sum(
                    [item[0] * item[1] for item in zip(self.m[x], mat_t[y])]
                )
        return mulmat

    def __matmul__(self, rhs):
        return self * rhs

    def __imul__(self, rhs):

        tmp = copy.deepcopy(self)
        mat_t = rhs.get_transpose()
        for x in range(3):
            for y in range(3):
                tmp[x][y] = sum(
                    [item[0] * item[1] for item in zip(self.m[x], mat_t[y])]
                )
        self.m = tmp.m.copy()
        return self

    def __imatmul__(self, rhs):
        self *= rhs
        return self

    def __rmul__(self, rhs):
        temp = Vec3()
        temp.x = rhs.x * self.m[0][0] + rhs.y * self.m[1][0] + rhs.z * self.m[2][0]
        temp.y = rhs.x * self.m[0][1] + rhs.y * self.m[1][1] + rhs.z * self.m[2][1]
        temp.z = rhs.x * self.m[0][2] + rhs.y * self.m[1][2] + rhs.z * self.m[2][2]
        return temp
