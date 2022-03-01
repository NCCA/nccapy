"""
Simple Mat3 class which can be used with the Vec3 class
"""

import copy
import functools
import math
import operator
import json


class Mat3Error(Exception):
    """An exception class for Mat3"""

    pass


class Mat3NotSquare(Exception):
    """Make sure we have 3x3"""

    pass


_identity = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]


class Mat3:
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
        v = Mat3()
        return v

    @classmethod
    def zero(cls):
        "class method to return a zero matrix"
        v = Mat3()
        v.m = [[0.0] * 3] * 3  # should we do this just because we can? ;-) 3x3 list of zeros
        return v

    @classmethod
    def from_list(cls, l):
        "class method to create mat3 from list"
        v = Mat3()
        v.m = l
        if v._is_square() is not True:
            if len(l) == 9:  # can convert
                v.m = [l[0:3], l[3:6], l[6:]]
                return v
            else:
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

    @classmethod
    def scale(cls, x: float, y: float, z: float):
        "return a scale matrix resetting to identity first"
        s = Mat3()
        s.m[0][0] = x
        s.m[1][1] = y
        s.m[2][2] = z
        return s

    @classmethod
    def rotateX(cls, angle: float):
        "return a rotation around the X axis by angle degrees"
        x = Mat3()
        beta = math.radians(angle)
        sr = math.sin(beta)
        cr = math.cos(beta)
        x.m[1][1] = cr
        x.m[1][2] = sr
        x.m[2][1] = -sr
        x.m[2][2] = cr
        return x

    @classmethod
    def rotateY(self, angle: float):
        "return a rotation around the y axis by angle degrees"
        y = Mat3()
        beta = math.radians(angle)
        sr = math.sin(beta)
        cr = math.cos(beta)
        y.m[0][0] = cr
        y.m[0][2] = -sr
        y.m[2][0] = sr
        y.m[2][2] = cr
        return y

    @classmethod
    def rotateZ(self, angle: float):
        "return a rotation around the Z axis by angle degrees"
        z = Mat3()
        beta = math.radians(angle)
        sr = math.sin(beta)
        cr = math.cos(beta)
        z.m[0][0] = cr
        z.m[0][1] = sr
        z.m[1][0] = -sr
        z.m[1][1] = cr
        return z

    def __getitem__(self, idx):
        "access array elements remember this is a list of lists [[3],[3],[3]]"
        return self.m[idx]

    def __setitem__(self, idx, item):
        "set items remember this is a list of lists [[3],[3],[3]]"
        self.m[idx] = item

    def __mul__(self, rhs):
        if isinstance(rhs, (int, float)):
            for i in len(self.m):
                for j in len(self.m[i]):
                    self.m[i][j] *= rhs
            return self
        raise Mat3Error

    def _mat_mul(self, rhs):
        "matrix mult internal function"
        # fmt: off
        a00 = self.m[0][0] # cache values for speed? (works in C++ not sure about python)
        a01 = self.m[0][1]
        a02 = self.m[0][2] 
        a10 = self.m[1][0]
        a11 = self.m[1][1] 
        a12 = self.m[1][2] 
        a20 = self.m[2][0]
        a21 = self.m[2][1]
        a22 = self.m[2][2] 
        
        b00 = rhs.m[0][0]
        b01 = rhs.m[0][1]
        b02 = rhs.m[0][2] 
        b10 = rhs.m[1][0]
        b11 = rhs.m[1][1] 
        b12 = rhs.m[1][2] 
        b20 = rhs.m[2][0]
        b21 = rhs.m[2][1]
        b22 = rhs.m[2][2] 

        ret=Mat3() # result mat4 
        ret.m[0][0] = b00 * a00 + b01 * a10 + b02 * a20 
        ret.m[0][1] = b00 * a01 + b01 * a11 + b02 * a21 
        ret.m[0][2] = b00 * a02 + b01 * a12 + b02 * a22 
        ret.m[1][0] = b10 * a00 + b11 * a10 + b12 * a20 
        ret.m[1][1] = b10 * a01 + b11 * a11 + b12 * a21 
        ret.m[1][2] = b10 * a02 + b11 * a12 + b12 * a22 
        ret.m[2][0] = b20 * a00 + b21 * a10 + b22 * a20 
        ret.m[2][1] = b20 * a01 + b21 * a11 + b22 * a21 
        ret.m[2][2] = b20 * a02 + b21 * a12 + b22 * a22 
        return ret
        # fmt: on

    def __matmul__(self, rhs):
        from .Vec3 import Vec3  # note relative import

        "multiply matrix by another matrix"
        if isinstance(rhs, Mat3):
            return self._mat_mul(rhs)
        elif isinstance(rhs, Vec3):
            return Vec3(
                rhs.x * self.m[0][0] + rhs.y * self.m[0][1] + rhs.z * self.m[0][2],
                rhs.x * self.m[1][0] + rhs.y * self.m[1][1] + rhs.z * self.m[1][2],
                rhs.x * self.m[2][0] + rhs.y * self.m[2][1] + rhs.z * self.m[2][2],
            )
        else:
            raise Mat3Error

    def __add__(self, rhs):
        "piecewise addition of elements"
        temp = Mat3()
        for i in range(0, len(temp.m)):
            temp.m[i] = [a + b for a, b in zip(self.m[i], rhs.m[i])]
        return temp

    def __iadd__(self, rhs):
        "piecewise addition of elements to this"
        for i in range(0, len(self.m)):
            self.m[i] = [a + b for a, b in zip(self.m[i], rhs.m[i])]
        return self

    def __sub__(self, rhs):
        "piecewise subtraction of elements"
        temp = Mat3()
        for i in range(0, len(temp.m)):
            temp.m[i] = [a - b for a, b in zip(self.m[i], rhs.m[i])]
        return temp

    def __isub__(self, rhs):
        "piecewise subtraction of elements to this"
        for i in range(0, len(self.m)):
            self.m[i] = [a - b for a, b in zip(self.m[i], rhs.m[i])]
        return self

    def determinant(self):
        "determinant of matrix"
        return (
            +self.m[0][0] * (self.m[1][1] * self.m[2][2] - self.m[2][1] * self.m[1][2])
            - self.m[0][1] * (self.m[1][0] * self.m[2][2] - self.m[1][2] * self.m[2][0])
            + self.m[0][2] * (self.m[1][0] * self.m[2][1] - self.m[1][1] * self.m[2][0])
        )

    def inverse(self):
        "Inverse of matrix raise MatrixError if not calculable"
        det = self.determinant()
        try:
            invdet = 1 / det
            tmp = Mat3()
            # minor matrix + cofactor
            tmp.m[0][0] = +(self.m[1][1] * self.m[2][2] - self.m[1][2] * self.m[2][1]) * invdet
            tmp.m[1][0] = -(self.m[1][0] * self.m[2][2] - self.m[1][2] * self.m[2][0]) * invdet
            tmp.m[2][0] = +(self.m[1][0] * self.m[2][1] - self.m[1][1] * self.m[2][0]) * invdet

            tmp.m[0][1] = -(self.m[0][1] * self.m[2][2] - self.m[0][2] * self.m[2][1]) * invdet
            tmp.m[1][1] = +(self.m[0][0] * self.m[2][2] - self.m[0][2] * self.m[2][0]) * invdet
            tmp.m[2][1] = -(self.m[0][0] * self.m[2][1] - self.m[0][1] * self.m[2][0]) * invdet

            tmp.m[0][2] = +(self.m[0][1] * self.m[1][2] - self.m[0][2] * self.m[1][1]) * invdet
            tmp.m[1][2] = -(self.m[0][0] * self.m[1][2] - self.m[0][2] * self.m[1][0]) * invdet
            tmp.m[2][2] = +(self.m[0][0] * self.m[1][1] - self.m[0][1] * self.m[1][0]) * invdet

            return tmp
        except:
            raise Mat3Error

    def __str__(self):
        return f"[{self.m[0]}\n{self.m[1]}\n{self.m[2]}]"

    def to_json(self):
        return json.dumps(
            self, default=lambda o: {key: getattr(self, key, None) for key in self.__slots__}, sort_keys=True, indent=4
        )
