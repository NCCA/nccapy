import math
import os
import unittest
from os.path import exists

from Geo.Obj import Obj
from Math.Mat4 import Mat4
from Math.Vec3 import Vec3


class TestObj(unittest.TestCase):
    validfiles = [
        "tests/files/Triangle1.obj",
        "tests/files/TriangleVertNormal.obj",
        "tests/files/TriangleVertsOnly.obj",
        "tests/files/TriangleVertsUV.obj",
        "tests/files/Triangle3UV.obj",
        "tests/files/TriMessedFormat.obj",
        "tests/files/CubeNegativeIndex.obj",
    ]
    invalidfiles = ["files/BrokenFloats.obj"]

    def setUp(self):
        pass

    def test_ctor(self):
        o = Obj()
        self.assertEqual(len(o.faces), 0)
        self.assertEqual(len(o.verts), 0)
        self.assertEqual(len(o.normals), 0)
        self.assertEqual(len(o.uv), 0)

    def test_load_valid(self):
        o = Obj()
        for file in self.validfiles:
            self.assertTrue(o.load(file))

    def test_load_not_found(self):
        o = Obj()
        with self.assertRaises(FileNotFoundError):
            o.load("bogus.obj")
