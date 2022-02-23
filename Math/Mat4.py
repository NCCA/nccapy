"""
Simple Mat4 class which can be used with the Vec3 class
"""

import copy
import functools
import math
import operator


class Mat4Error(Exception):
    """An exception class for Mat3"""

    pass


class Mat4NotSquare(Exception):
    """Make sure we have 3x3"""

    pass


_identity = [
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 1.0],
]


class Mat4:
    __slots__ = ["m"]

    def __init__(self):
        "construct to identity matrix"
        self.m = copy.deepcopy(_identity)

    def get_matrix(self):
        "return matrix elements as list ideal for OpenGL etc"
        return functools.reduce(operator.concat, self.m)

    @classmethod
    def identity(cls):
        "class method to return a new identity matrix"
        v = Mat4()
        return v

    @classmethod
    def zero(cls):
        "class method to return a zero matrix"
        v = Mat4()
        v.m = [[0.0] * 4] * 4  # should we do this because we can 4x4 zeros ;-)
        return v

    @classmethod
    def from_list(cls, l):
        "class method to create mat3 from list"
        v = Mat4()
        v.m = l
        if v._is_square() is not True:
            if len(l) == 16:  # can convert
                v.m = [l[0:5], l[5:8], l[8:12], l[12:16]]
                return v
            else:
                raise Mat4NotSquare
        else:
            return v

    def _is_square(self) -> bool:
        "ensure matrix is square"
        return len(self.m) == 4 and all(len(i) == 4 for i in self.m)

    def transpose(self):
        "traspose this matrix"
        self.m = [list(item) for item in zip(*self.m)]

    def get_transpose(self):
        "return a new matrix as the transpose of ourself"
        m = Mat4()
        m.m = [list(item) for item in zip(*self.m)]
        return m

    def scale(self, x: float, y: float, z: float):
        "set this matrix to be a scale matrix resetting to identity first"
        self.m = copy.deepcopy(_identity)
        self.m[0][0] = x
        self.m[1][1] = y
        self.m[2][2] = z


    def rotateX(self,angle) :
        "set this matrix to be a rotation around the X axis by angle degrees"
        self.m = copy.deepcopy(_identity)
        beta = math.radians(angle)
        sr = math.sin(beta)
        cr = math.cos(beta)
        self.m[1][1] = cr
        self.m[1][2] = sr
        self.m[2][1] = -sr  
        self.m[2][2] = cr