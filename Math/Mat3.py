"""
Simple Mat3 class which can be used with the Vec3 class
"""

import copy
import functools
import math
import operator


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
        v.m = [
            [0.0] * 3
        ] * 3  # should we do this just because we can? ;-) 3x3 list of zeros
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

    def scale(self, x: float, y: float, z: float):
        "set this matrix to be a scale matrix resetting to identity first"
        self.m = copy.deepcopy(_identity)

        self.m[0][0] = x
        self.m[1][1] = y
        self.m[2][2] = z

    def rotateX(self, angle: float):
        "set this matrix to be a rotation around the X axis by angle degrees"
        self.m = copy.deepcopy(_identity)
        beta = math.radians(angle)
        sr = math.sin(beta)
        cr = math.cos(beta)
        self.m[1][1] = cr
        self.m[1][2] = sr
        self.m[2][1] = -sr
        self.m[2][2] = cr

    def rotateY(self, angle: float):
        "set this matrix to be a rotation around the y axis by angle degrees"
        self.m = copy.deepcopy(_identity)

        beta = math.radians(angle)
        sr = math.sin(beta)
        cr = math.cos(beta)
        self.m[0][0] = cr
        self.m[0][2] = -sr
        self.m[2][0] = sr
        self.m[2][2] = cr

    def rotateZ(self, angle: float):
        "set this matrix to be a rotation around the Z axis by angle degrees"
        self.m = copy.deepcopy(_identity)

        beta = math.radians(angle)
        sr = math.sin(beta)
        cr = math.cos(beta)
        self.m[0][0] = cr
        self.m[0][1] = sr
        self.m[1][0] = -sr
        self.m[1][1] = cr

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

    def __matmul__(self, rhs):
        from Math.Vec3 import Vec3

        "multiply matrix by another matrix"
        if isinstance(rhs, Mat3):
            mat_t = rhs.get_transpose()
            mulmat = Mat3()
            for x in range(3):
                for y in range(3):
                    mulmat[x][y] = sum(
                        [item[0] * item[1] for item in zip(self.m[x], mat_t[y])]
                    )
            return mulmat
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
            tmp.m[0][0] = (
                self.m[1][1] * self.m[2][2] - self.m[2][1] * self.m[1][2]
            ) * invdet
            tmp.m[0][1] = (
                -(self.m[1][0] * self.m[2][2] - self.m[1][2] * self.m[2][0]) * invdet
            )
            tmp.m[0][2] = (
                self.m[1][0] * self.m[2][1] - self.m[2][0] * self.m[1][1]
            ) * invdet

            tmp.m[1][0] = (
                -(self.m[0][1] * self.m[2][2] - self.m[0][2] * self.m[2][1]) * invdet
            )
            tmp.m[1][1] = (
                self.m[0][0] * self.m[2][2] - self.m[0][2] * self.m[2][0]
            ) * invdet
            tmp.m[1][2] = (
                -(self.m[0][0] * self.m[2][1] - self.m[2][0] * self.m[0][1]) * invdet
            )

            tmp.m[2][0] = (
                self.m[0][1] * self.m[1][2] - self.m[0][2] * self.m[1][1]
            ) * invdet
            tmp.m[2][1] = (
                -(self.m[0][0] * self.m[1][2] - self.m[1][0] * self.m[0][2]) * invdet
            )
            tmp.m[2][2] = (
                self.m[0][0] * self.m[1][1] - self.m[1][0] * self.m[0][1]
            ) * invdet

            return tmp
        except:
            raise Mat3Error

    def __str__(self):
        return f"[{self.m[0]}\n{self.m[1]}\n{self.m[2]}]"
