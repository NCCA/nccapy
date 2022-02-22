import math
import unittest

from Math.Vec3 import Vec3


class TestVec3(unittest.TestCase):
    def test_ctor(self):
        v = Vec3()
        self.assertAlmostEqual(v.x, 0.0)
        self.assertAlmostEqual(v.y, 0.0)
        self.assertAlmostEqual(v.z, 0.0)

    def test_userCtor(self):
        v = Vec3(2.0, 3.0, 4.0)
        self.assertAlmostEqual(v.x, 2.0)
        self.assertAlmostEqual(v.y, 3.0)
        self.assertAlmostEqual(v.z, 4.0)

    def test_ctor_single_value(self):
        v = Vec3(x=2.0)
        self.assertAlmostEqual(v.x, 2.0)
        self.assertAlmostEqual(v.y, 0)
        self.assertAlmostEqual(v.z, 0)

        v = Vec3(y=2.0)
        self.assertAlmostEqual(v.x, 0.0)
        self.assertAlmostEqual(v.y, 2.0)
        self.assertAlmostEqual(v.z, 0)

        v = Vec3(z=2.0)
        self.assertAlmostEqual(v.x, 0.0)
        self.assertAlmostEqual(v.y, 0)
        self.assertAlmostEqual(v.z, 2.0)

    def test_add(self):
        a = Vec3(1, 2, 3)
        b = Vec3(4, 5, 6)
        c = a + b
        self.assertAlmostEqual(c.x, 5)
        self.assertAlmostEqual(c.y, 7)
        self.assertAlmostEqual(c.z, 9)

    def test_set(self):
        a = Vec3()
        a.set(2.5, 0.1, 0.5)
        self.assertAlmostEqual(a.x, 2.5)
        self.assertAlmostEqual(a.y, 0.1)
        self.assertAlmostEqual(a.z, 0.5)

    def test_error_set(self):
        self.assertRaises(ValueError, Vec3.set, self, 2, 3, "hello")

    def test_dot(self):
        a = Vec3(1.0, 2.0, 3.0)
        b = Vec3(4.0, 5.0, 6.0)
        self.assertAlmostEqual(a.dot(b), 32.0)

    def test_length(self):
        a = Vec3(22, 1, 32)
        self.assertAlmostEqual(a.length(), 38.845, places=2)

    def test_normalize(self):
        a = Vec3(22.3, 0.5, 10.0)
        a.normalize()
        self.assertAlmostEqual(a.x, 0.912266, places=5)
        self.assertAlmostEqual(a.y, 0.0204544, places=5)
        self.assertAlmostEqual(a.z, 0.409088, places=5)

    def test_equal(self):
        a = Vec3(0.1, 0.2, 0.3)
        b = Vec3(0.1, 0.2, 0.3)
        self.assertTrue(a == b)

    def test_not_equal(self):
        a = Vec3(0.3, 0.4, 0.3)
        b = Vec3(0.1, 0.2, 0.3)
        self.assertTrue(a != b)

    def test_inner(self):
        a = Vec3(1.0, 2.0, 3.0)
        b = Vec3(3.0, 4.0, 5.0)
        self.assertAlmostEqual(a.inner(b), 26.0)

    def test_length_squared(self):
        a = Vec3(22, 1, 32)
        self.assertAlmostEqual(a.length_squared(), 1509.0)

    def test_reflect(self):
        N = Vec3(0, 1, 0)
        a = Vec3(2, 2, 0)
        a.normalize()
        ref = a.reflect(N)
        self.assertAlmostEqual(ref.x, 0.707, places=3)
        self.assertAlmostEqual(ref.y, -0.707, places=3)
        self.assertAlmostEqual(ref.z, 0)

    def test_clamp(self):
        a = Vec3(0.1, 5.0, 1.7)
        a.clamp(0.5, 1.8)
        self.assertAlmostEqual(a.x, 0.5)
        self.assertAlmostEqual(a.y, 1.8)
        self.assertAlmostEqual(a.z, 1.7)

    def test_outer(self):
        a = Vec3(1.0, 2.0, 3.0)
        b = Vec3(3.0, 4.0, 5.0)
        outer = a.outer(b)
        result = [3, 4, 5, 6, 8, 10, 9, 12, 15]
        value = outer.get_matrix()
        for r, v in zip(result, value):
            self.assertAlmostEqual(r, v, places=6)

    def test_null(self):
        a = Vec3(2, 3, 5)
        a.null()
        self.assertAlmostEqual(a.x, 0.0)
        self.assertAlmostEqual(a.y, 0.0)
        self.assertAlmostEqual(a.z, 0.0)

    def test_cross(self):
        a = Vec3(0.0, 1.0, 0.0)
        b = Vec3(-1.0, 0.0, 0.0)
        c = a.cross(b)
        self.assertEqual(c, Vec3(0.0, 0.0, 1.0))

    def test_getAttr(self):
        a = Vec3(1, 2, 3)
        self.assertAlmostEqual(getattr(a, "x"), 1.0)
        self.assertAlmostEqual(getattr(a, "y"), 2.0)
        self.assertAlmostEqual(getattr(a, "z"), 3.0)
        # check to see if we can get non attr
        self.assertRaises(AttributeError, getattr, a, "b")
        # check to see that adding an attrib fails
        self.assertRaises(AttributeError, setattr, a, "b", 20.0)
