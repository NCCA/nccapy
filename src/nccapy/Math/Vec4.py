"""
Simple Float only Vec3 class for 3D graphics, very similar to the pyngl ones
"""

import math


class Vec4:
    __slots__ = ["_x", "_y", "_z", "_w"]
    "by using slots we fix our class attributes to x,y,z,w"

    def __init__(self, x=0.0, y=0.0, z=0.0, w=1.0):
        """simple ctor"""
        self._x = x  # x component of vector : float
        self._y = y  # y component of vector : float
        self._z = z  # z component of vector : float
        self._w = w  # w component of vector : float

    def _validate_and_set(self, v, name):
        """
        check if v is a float or int
        Args:
            v (number): The value to check.
        Raises:
            ValueError: If v is not a float or int.
        """
        if not isinstance(v, (int, float)):
            raise ValueError("need float or int")
        else:
            setattr(self, name, v)

    @property
    def x(self):
        """
        The x-coordinate of the vector.
        """
        return self._x

    @x.setter
    def x(self, x):
        """
        The x-coordinate of the vector.
        """
        self._validate_and_set(x, "_x")

    @property
    def y(self):
        """
        The y-coordinate of the vector.
        """
        return self._y

    @y.setter
    def y(self, y):
        """
        The y-coordinate of the vector.
        """
        self._validate_and_set(y, "_y")

    @property
    def z(self):
        """
        The z-coordinate of the vector.
        """
        return self._z

    @z.setter
    def z(self, z):
        """
        The z-coordinate of the vector.
        """
        self._validate_and_set(z, "_z")

    @property
    def w(self):
        """
        The w-coordinate of the vector.
        """
        return self._w

    @w.setter
    def w(self, w):
        """
        The w-coordinate of the vector.
        """
        self._validate_and_set(w, "_w")

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
        length = self.length()
        try:
            self.x /= length
            self.y /= length
            self.z /= length
            self.w /= length
        except ZeroDivisionError:
            raise ZeroDivisionError("cannot normalize the zero vector")

    def __eq__(self, rhs):
        "test a==b using math.isclose"
        if not isinstance(rhs, Vec4):
            return NotImplemented
        return (
            math.isclose(self.x, rhs.x)
            and math.isclose(self.y, rhs.y)
            and math.isclose(self.z, rhs.z)
            and math.isclose(self.w, rhs.w)
        )

    def __neq__(self, rhs):
        "test a==b using math.isclose"
        if not isinstance(rhs, Vec4):
            return NotImplemented
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

    def __mul__(self, rhs):
        if isinstance(rhs, (float, int)):
            self.x *= rhs
            self.y *= rhs
            self.z *= rhs
            self.w *= rhs
            return self
        else:
            raise ValueError

    def __rmul__(self, rhs):
        return self * rhs

    def __matmul__(self, rhs):
        "Vec4 @ Mat4 matrix multiplication"
        return Vec4(
            self.x * rhs.m[0][0]
            + self.y * rhs.m[1][0]
            + self.z * rhs.m[2][0]
            + self.w * rhs.m[3][0],
            self.x * rhs.m[0][1]
            + self.y * rhs.m[1][1]
            + self.z * rhs.m[2][1]
            + self.w * rhs.m[3][1],
            self.x * rhs.m[0][2]
            + self.y * rhs.m[1][2]
            + self.z * rhs.m[2][2]
            + self.w * rhs.m[3][2],
            self.x * rhs.m[0][3]
            + self.y * rhs.m[1][3]
            + self.z * rhs.m[2][3]
            + self.w * rhs.m[3][3],
        )

    def __repr__(self):
        "repr for debugging purposes"
        return f"Vec4 [{self.x},{self.y},{self.z},{self.w}]"

    def __str__(self):
        "print out the vector as a string"
        return f"[{self.x},{self.y},{self.z},{self.w}]"
