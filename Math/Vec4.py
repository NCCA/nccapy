"""
Simple Float only Vec3 class for 3D graphics, very similar to the pyngl ones
"""
import math

from nccapy.Math.Util import clamp


class Vec4:

    __slots__ = ["x", "y", "z", "w"]
    "by using slots we fix our class attributes to x,y,z,W"

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, w: float = 1.0):
        """simple ctor"""
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __add__(self, rhs):
        "return a+b vector addition"
        r = Vec4()
        r.x = self.x + rhs.x
        r.y = self.y + rhs.y
        r.z = self.z + rhs.z
        r.w = self.w + rhs.w
        return r

    def __iadd__(self, rhs):
        "return a+=b vector addition"
        self.x += rhs.x
        self.y += rhs.y
        self.z += rhs.z
        self.w += rhs.w

        return self

    def __sub__(self, rhs):
        "return a+b vector addition"
        r = Vec4()
        r.x = self.x - rhs.x
        r.y = self.y - rhs.y
        r.z = self.z - rhs.z
        r.w = self.w - rhs.w
        return r

    def __isub__(self, rhs):
        "return a+=b vector addition"
        self.x -= rhs.x
        self.y -= rhs.y
        self.z -= rhs.z
        self.w -= rhs.w
        return self

    def set(self, x, y, z, w=1.0):
        "set from x,y,z,w will convert to float an raise value error if problem"
        try:
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)
            self.w = float(w)
        except ValueError:
            print("need float values")
            raise

    def dot(self, rhs):
        return (self.x * rhs.x) + (self.y * rhs.y) + (self.z * rhs.z) + (self.w * rhs.w)

    def length(self):
        "length of vector"
        return math.sqrt(self.x**2 + self.y**2 + self.z**2 + self.w**2)

    def length_squared(self):
        "square length of vector"
        return self.x**2 + self.y**2 + self.z**2 + self.w**2

    def normalize(self):
        "normalize this vector"
        len = self.length()
        try:
            self.x /= len
            self.y /= len
            self.z /= len
            self.w /= len
        except ZeroDivisionError:
            raise

    def __eq__(self, rhs):
        "test a==b using math.isclose"
        return (
            math.isclose(self.x, rhs.x)
            and math.isclose(self.y, rhs.y)
            and math.isclose(self.z, rhs.z)
            and math.isclose(self.w, rhs.w)
        )

    def __neq__(self, rhs):
        "test a==b using math.isclose"
        return (
            math.isclose(self.x, rhs.x)
            or math.isclose(self.y, rhs.y)
            or math.isclose(self.z, rhs.z)
            or math.isclose(self.w, rhs.w)
        )

    def __neg__(self):
        self.x = -self.x
        self.y = -self.y
        self.z = -self.z
        self.w = -self.w
        return self

    def __repr__(self):
        "may update to f-strings soon"
        return "Vec4 [{},{},{},{}]".format(self.x, self.y, self.z, self.z)

    def __str__(self):
        "may update to f-strings soon"
        return "[{},{},{},{}]".format(self.x, self.y, self.z, self.w)