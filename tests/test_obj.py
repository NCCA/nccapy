import math
import os
import unittest
from os.path import exists

from Geo.Obj import Face, Obj
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

    def test_parse_vertex(self):
        obj = Obj.from_file("tests/files/Triangle1.obj")
        self.assertEqual(len(obj.verts), 3)

    def test_parse_normal(self):
        obj = Obj.from_file("tests/files/Triangle1.obj")
        self.assertEqual(len(obj.normals), 3)

    def test_parse_uv(self):
        obj = Obj.from_file("tests/files/Triangle1.obj")
        self.assertEqual(len(obj.uv), 3)

    def test_check_verts(self):
        obj = Obj.from_file("tests/files/Triangle1.obj")

        result = [Vec3(2.0, 0.0, 0.0), Vec3(0.0, 4.0, 0.0), Vec3(-2.0, 0.0, 0.0)]
        for r, v in zip(result, obj.verts):
            self.assertEqual(r, v)

    def test_check_normals(self):
        obj = Obj.from_file("tests/files/Triangle1.obj")

        result = [Vec3(0.0, 0.0, 1.0), Vec3(0.0, 0.0, 1.0), Vec3(0.0, 0.0, 1.0)]
        for r, v in zip(result, obj.normals):
            self.assertEqual(r, v)

    def test_check_uvs(self):
        obj = Obj.from_file("tests/files/Triangle1.obj")

        result = [
            Vec3(1.0, 0.0, 0.0),
            Vec3(0.5, 1.0, 0.0),
            Vec3(0.004399, 0.008916, 0.0),
        ]
        for r, v in zip(result, obj.uv):
            self.assertEqual(r, v)

    def test_check_face_vert_only(self):
        obj = Obj.from_file("tests/files/TriangleVertsOnly.obj")
        # face is f 1/1/1 2/2/2 3/3/3 but we index from 0
        self.assertEqual(obj.faces[0].vert[0], 0)
        self.assertEqual(obj.faces[0].vert[1], 1)
        self.assertEqual(obj.faces[0].vert[2], 2)

    def test_check_face_vert_normal(self):
        obj = Obj.from_file("tests/files/TriangleVertNormal.obj")
        self.assertEqual(obj.faces[0].vert[0], 0)
        self.assertEqual(obj.faces[0].vert[1], 1)
        self.assertEqual(obj.faces[0].vert[2], 2)
        self.assertEqual(obj.faces[0].normal[0], 0)
        self.assertEqual(obj.faces[0].normal[1], 1)
        self.assertEqual(obj.faces[0].normal[2], 2)

    def test_check_face_vert_uv(self):
        obj = Obj.from_file("tests/files/TriangleVertsUV.obj")
        self.assertEqual(obj.faces[0].vert[0], 0)
        self.assertEqual(obj.faces[0].vert[1], 1)
        self.assertEqual(obj.faces[0].vert[2], 2)
        self.assertEqual(obj.faces[0].uv[0], 0)
        self.assertEqual(obj.faces[0].uv[1], 1)
        self.assertEqual(obj.faces[0].uv[2], 2)

    def test_check_face_vert_only_negative_index(self):
        obj = Obj.from_file("tests/files/CubeNegativeIndex.obj")
        # face is f -4 -3 -2 -1
        idx = 0
        for i in range(0, len(obj.faces)):
            self.assertEqual(obj.faces[i].vert[0], idx)
            self.assertEqual(obj.faces[i].vert[1], idx + 1)
            self.assertEqual(obj.faces[i].vert[2], idx + 2)
            self.assertEqual(obj.faces[i].vert[3], idx + 3)
            idx += 4

    def test_check_face(self):
        obj = Obj.from_file("tests/files/Triangle1.obj")
        # face is f 1/1/1 2/2/2 3/3/3 but we index from 0
        for i in range(0, 3):
            self.assertEqual(obj.faces[0].vert[i], i)
            self.assertEqual(obj.faces[0].normal[i], i)
            self.assertEqual(obj.faces[0].uv[i], i)

    def test_add_vertex(self):
        obj = Obj()
        for i in range(0, 20):
            obj.add_vertex(Vec3(i, i, i))
        for i in range(0, 20):
            self.assertEqual(Vec3(i, i, i), obj.verts[i])

    def test_add_normal(self):
        obj = Obj()
        for i in range(0, 20):
            obj.add_normal(Vec3(i, i, i))
        for i in range(0, 20):
            self.assertEqual(Vec3(i, i, i), obj.normals[i])

    def test_add_uv(self):
        obj = Obj()
        for i in range(0, 20):
            obj.add_uv(Vec3(i, i, i))
        for i in range(0, 20):
            self.assertEqual(Vec3(i, i, i), obj.uv[i])

    def test_add_face(self):
        f = Face()
        obj = Obj()
        for i in range(0, 3):
            f.vert.append(i)
            f.normal.append(i)
            f.uv.append(i)
        obj.add_face(f)
        for i in range(0, 3):
            self.assertEqual(obj.faces[0].vert[i], i)
            self.assertEqual(obj.faces[0].normal[i], i)
            self.assertEqual(obj.faces[0].uv[i], i)

    def test_build_obj(self):
        obj = Obj()
        obj.add_vertex(Vec3(2.0, 0.0, 0.0))
        obj.add_vertex(Vec3(0.0, 4.0, 0.0))
        obj.add_vertex(Vec3(-2.0, 0.0, 0.0))
        obj.add_uv(Vec3(1.0, 0.0, 0.0))
        obj.add_uv(Vec3(0.5, 1.0, 0.0))
        obj.add_uv(Vec3(0.004399, 0.008916, 0.0))
        obj.add_normal(Vec3(0.0, 0.0, 1.0))
        # f 1/1/1 2/2/1 3/3/1
        face = Face()
        face.vert.append(0)
        face.vert.append(1)
        face.vert.append(2)
        face.uv.append(0)
        face.uv.append(1)
        face.uv.append(2)
        face.normal.append(0)
        face.normal.append(0)
        face.normal.append(0)
        obj.add_face(face)
        obj.save("tests/tempObj.obj")
        # reload and check
        new = Obj.from_file("tests/tempObj.obj")
        self.assertEqual(new.verts[0], Vec3(2.0, 0.0, 0.0))
        self.assertEqual(new.verts[1], Vec3(0.0, 4.0, 0.0))
        self.assertEqual(new.verts[2], Vec3(-2.0, 0.0, 0.0))
        self.assertEqual(new.uv[0], Vec3(1.0, 0.0, 0.0))
        self.assertEqual(new.uv[1], Vec3(0.5, 1.0, 0.0))
        self.assertEqual(new.uv[2], Vec3(0.004399, 0.008916, 0.0))
        self.assertEqual(new.normals[0], Vec3(0.0, 0.0, 1.0))
        self.assertEqual(new.faces[0].vert, [0, 1, 2])
        self.assertEqual(new.faces[0].uv, [0, 1, 2])
        self.assertEqual(new.faces[0].normal, [0, 0, 0])
