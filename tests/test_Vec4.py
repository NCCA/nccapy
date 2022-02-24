import math
import unittest

from Math.Vec4 import Vec4
from Math.Mat4 import Mat4


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

    def test_sub(self):
        a = Vec4(1, 2, 3)
        b = Vec4(4, 5, 6)
        c = a - b
        self.assertAlmostEqual(c.x, -3)
        self.assertAlmostEqual(c.y, -3)
        self.assertAlmostEqual(c.z, -3)
        self.assertAlmostEqual(c.w, 0)

    def test_sub_equals(self):
        a = Vec4(1, 2, 3)
        b = Vec4(4, 5, 6)
        a -= b
        self.assertAlmostEqual(a.x, -3)
        self.assertAlmostEqual(a.y, -3)
        self.assertAlmostEqual(a.z, -3)
        self.assertAlmostEqual(a.w, 0)

    def test_set(self):
        a = Vec4()
        a.set(2.5, 0.1, 0.5, 0.2)
        self.assertAlmostEqual(a.x, 2.5)
        self.assertAlmostEqual(a.y, 0.1)
        self.assertAlmostEqual(a.z, 0.5)
        self.assertAlmostEqual(a.w, 0.2)

    def test_error_set(self):
        with (self.assertRaises(ValueError)):
            a = Vec4()
            a.set("a", 2, 3, 5)

    def test_dot(self):
        a = Vec4(1.0, 2.0, 3.0, 4.0)
        b = Vec4(5.0, 6.0, 7.0, 8.0)
        self.assertAlmostEqual(a.dot(b), 70.0)

    def test_length(self):
        a = Vec4(22, 1, 32, 12)
        self.assertAlmostEqual(a.length(), 40.657, places=3)

    def test_length_squared(self):
        a = Vec4(22, 1, 32, 12)
        self.assertAlmostEqual(a.length_squared(), 1653, places=2)

    def test_normalize(self):
        a = Vec4(25.0, 12.2, 0.5, -2.0)
        a.normalize()
        self.assertAlmostEqual(a.x, 0.8962, places=3)
        self.assertAlmostEqual(a.y, 0.4373, places=3)
        self.assertAlmostEqual(a.z, 0.0179, places=3)
        self.assertAlmostEqual(a.w, -0.0716, places=3)

    def test_equal(self):
        a = Vec4(0.1, 0.2, 0.3, 0.4)
        b = Vec4(0.1, 0.2, 0.3, 0.4)
        self.assertTrue(a == b)

    def test_not_equal(self):
        a = Vec4(0.3, 0.4, 0.3)
        b = Vec4(0.1, 0.2, 0.3)
        self.assertTrue(a != b)

    def test_negate(self):
        a = Vec4(0.1, 0.5, -12, 5)
        a = -a
        self.assertAlmostEqual(a.x, -0.1)
        self.assertAlmostEqual(a.y, -0.5)
        self.assertAlmostEqual(a.z, 12.0)
        self.assertAlmostEqual(a.w, -5.0)

    def test_getAttr(self):
        a = Vec4(1, 2, 3, 5)
        self.assertAlmostEqual(getattr(a, "x"), 1.0)
        self.assertAlmostEqual(getattr(a, "y"), 2.0)
        self.assertAlmostEqual(getattr(a, "z"), 3.0)
        self.assertAlmostEqual(getattr(a, "w"), 5.0)
        # check to see if we can get non attr
        self.assertRaises(AttributeError, getattr, a, "b")
        # check to see that adding an attrib fails
        self.assertRaises(AttributeError, setattr, a, "b", 20.0)

    def test_mul_scalar(self):
        a = Vec4(1.0, 1.5, 2.0, 1.0)
        a = a * 2
        self.assertAlmostEqual(a.x, 2.0)
        self.assertAlmostEqual(a.y, 3.0)
        self.assertAlmostEqual(a.z, 4.0)
        self.assertAlmostEqual(a.w, 2.0)

        a = Vec4(1.5, 4.2, 2.8, 4.5)
        a = 2 * a
        self.assertAlmostEqual(a.x, 3.0)
        self.assertAlmostEqual(a.y, 8.4)
        self.assertAlmostEqual(a.z, 5.6)
        self.assertAlmostEqual(a.w, 9.0)

        with self.assertRaises(ValueError):
            a = a * "hello"

    def test_matmul(self):
        a = Vec4(1, 2, 3, 1)
        b = Mat4()
        b.rotateX(45.0)
        c = a @ b
        self.assertAlmostEqual(c.x, 1.0)
        self.assertAlmostEqual(c.y, -0.707107, places=4)
        self.assertAlmostEqual(c.z, 3.535534, places=4)
        self.assertAlmostEqual(c.w, 1.0)
