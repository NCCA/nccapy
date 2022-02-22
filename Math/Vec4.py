"""
Simple Float only Vec3 class for 3D graphics, very similar to the pyngl ones
"""
import math

from nccapy.Math.Util import clamp


class Vec4:

    __slots__ = ["x", "y", "z", "w"]
    "by using slots we fix our class attributes to x,y,z,W"

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0, w: float = 1.0):
        """will force float only construction raise ValueError if not capable"""
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
