import math
import unittest

from Math.Vec4 import Vec4


class TestVec4(unittest.TestCase):
    def test_ctor(self):
        v = Vec4()
        self.assertAlmostEqual(v.x, 0.0)
        self.assertAlmostEqual(v.y, 0.0)
        self.assertAlmostEqual(v.z, 0.0)
        self.assertAlmostEqual(v.w, 1.0)

    def test_userCtor(self):
        v = Vec4(2.0, 3.0, 4.0, 5.0)
        self.assertAlmostEqual(v.x, 2.0)
        self.assertAlmostEqual(v.y, 3.0)
        self.assertAlmostEqual(v.z, 4.0)
        self.assertAlmostEqual(v.w, 5.0)

    def test_ctor_single_value(self):
        v = Vec4(x=2.0)
        self.assertAlmostEqual(v.x, 2.0)
        self.assertAlmostEqual(v.y, 0.0)
        self.assertAlmostEqual(v.z, 0.0)
        self.assertAlmostEqual(v.w, 1.0)

        v = Vec4(y=2.0)
        self.assertAlmostEqual(v.x, 0.0)
        self.assertAlmostEqual(v.y, 2.0)
        self.assertAlmostEqual(v.z, 0.0)
        self.assertAlmostEqual(v.w, 1.0)

        v = Vec4(z=2.0)
        self.assertAlmostEqual(v.x, 0.0)
        self.assertAlmostEqual(v.y, 0.0)
        self.assertAlmostEqual(v.z, 2.0)
        self.assertAlmostEqual(v.w, 1.0)

        v = Vec4(w=9.2)
        self.assertAlmostEqual(v.x, 0.0)
        self.assertAlmostEqual(v.y, 0.0)
        self.assertAlmostEqual(v.z, 0.0)
        self.assertAlmostEqual(v.w, 9.2)

    def test_add(self):
        a = Vec4(1, 2, 3, 4)
        b = Vec4(5, 6, 7, 8)
        c = a + b
        self.assertAlmostEqual(c.x, 6.0)
        self.assertAlmostEqual(c.y, 8.0)
        self.assertAlmostEqual(c.z, 10.0)
        self.assertAlmostEqual(c.w, 12.0)
    def test_plus_equal(self):
        a = Vec4(1, 2, 3, 4)
        b = Vec4(5, 6, 7, 8)
        a += b
        self.assertAlmostEqual(a.x, 6.0)
        self.assertAlmostEqual(a.y, 8.0)
        self.assertAlmostEqual(a.z, 10.0)
        self.assertAlmostEqual(a.w, 12.0)
