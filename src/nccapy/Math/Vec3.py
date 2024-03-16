"""
Simple Float only Vec3 class for 3D graphics, very similar to the pyngl ones
"""

import json
import math

from .Util import clamp


class Vec3:
    __slots__ = ["x", "y", "z"]
    "by using slots we fix our class attributes to x,y,z"

    def __init__(self, x=0.0, y=0.0, z=0.0):
        """We prefer float here"""
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, rhs):
        "return a+b vector addition"
        r = Vec3()
        r.x = self.x + rhs.x
        r.y = self.y + rhs.y
        r.z = self.z + rhs.z
        return r

    def __iadd__(self, rhs):
        "return a+=b vector addition"
        self.x += rhs.x
        self.y += rhs.y
        self.z += rhs.z
        return self

    def __sub__(self, rhs):
        "return a+b vector addition"
        r = Vec3()
        r.x = self.x - rhs.x
        r.y = self.y - rhs.y
        r.z = self.z - rhs.z
        return r

    def __isub__(self, rhs):
        "return a+=b vector addition"
        self.x -= rhs.x
        self.y -= rhs.y
        self.z -= rhs.z
        return self

    def __eq__(self, rhs):
        "test a==b using math.isclose"
        if not isinstance(rhs, Vec3):
            return NotImplemented
        return (
            math.isclose(self.x, rhs.x)
            and math.isclose(self.y, rhs.y)
            and math.isclose(self.z, rhs.z)
        )

    def __neq__(self, rhs):
        "test a==b using math.isclose"
        if not isinstance(rhs, Vec3):
            return NotImplemented
        return (
            math.isclose(self.x, rhs.x)
            or math.isclose(self.y, rhs.y)
            or math.isclose(self.z, rhs.z)
        )

    def __neg__(self):
        self.x = -self.x
        self.y = -self.y
        self.z = -self.z
        return self

    def set(self, x, y, z):
        "set from x,y,z"
        try:
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)
        except ValueError:
            print("need float values")
            raise

    def dot(self, rhs):
        "return the dot product this vector with rhs"
        return self.x * rhs.x + self.y * rhs.y + self.z * rhs.z

    def length(self):
        "length of vector"
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def length_squared(self):
        "square length of vector"
        return self.x**2 + self.y**2 + self.z**2

    def inner(self, rhs):
        return (self.x * rhs.x) + (self.y * rhs.y) + (self.z * rhs.z)

    def null(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

    def cross(self, rhs):
        return Vec3(
            self.y * rhs.z - self.z * rhs.y,
            self.z * rhs.x - self.x * rhs.z,
            self.x * rhs.y - self.y * rhs.x,
        )

    def normalize(self):
        "normalize this vector"
        len = self.length()
        try:
            self.x /= len
            self.y /= len
            self.z /= len
        except ZeroDivisionError:
            raise

    def reflect(self, n):
        d = self.dot(n)
        #  I - 2.0 * dot(N, I) * N
        return Vec3(self.x - 2.0 * d * n.x, self.y - 2.0 * d * n.y, self.z - 2.0 * d * n.z)

    def clamp(self, low, high):
        self.x = clamp(self.x, low, high)
        self.y = clamp(self.y, low, high)
        self.z = clamp(self.z, low, high)

    def __repr__(self):
        "may update to f-strings soon"
        return "Vec3 [{},{},{}]".format(self.x, self.y, self.z)

    def __str__(self):
        "may update to f-strings soon"
        return "[{},{},{}]".format(self.x, self.y, self.z)

    def outer(self, rhs):
        from .Mat3 import Mat3

        return Mat3.from_list(
            [
                [self.x * rhs.x, self.x * rhs.y, self.x * rhs.z],
                [self.y * rhs.x, self.y * rhs.y, self.y * rhs.z],
                [self.z * rhs.x, self.z * rhs.y, self.z * rhs.z],
            ]
        )

    def __mul__(self, rhs):
        "piecewise scalar multiplication"
        if isinstance(rhs, (float, int)):
            self.x *= rhs
            self.y *= rhs
            self.z *= rhs
            return self
        else:
            raise ValueError

    def __rmul__(self, rhs):
        "piecewise scalar multiplication"
        return self * rhs

    def __matmul__(self, rhs):
        "Vec3 @ Mat3 matrix multiplication"
        return Vec3(
            self.x * rhs.m[0][0] + self.y * rhs.m[1][0] + self.z * rhs.m[2][0],
            self.x * rhs.m[0][1] + self.y * rhs.m[1][1] + self.z * rhs.m[2][1],
            self.x * rhs.m[0][2] + self.y * rhs.m[1][2] + self.z * rhs.m[2][2],
        )

    def to_json(self):
        a = {"Vec3": [self.x, self.y, self.z]}
        return json.dumps(a, sort_keys=True, indent=4)
