import unittest

from Math.Util import clamp
import math


class TestUtil(unittest.TestCase):
    def test_clamp(self):
        self.assertEquals(clamp(2,10,20),10) # test  int up
        self.assertEquals(clamp(200,10,20),20)# test int down
        self.assertAlmostEquals(clamp(0.1,0.01,1.0),0.1)
        self.assertAlmostEquals(clamp(2.1,0.01,1.2),1.2)
    def test_clamp_error(self):
        self.assertRaises(ValueError,clamp,1,100,0.1)
        