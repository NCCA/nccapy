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
      v = Vec4(2.0, 3.0, 4.0,5.0)
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


