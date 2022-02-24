import math
import unittest
from Math.Vec3 import Vec3 as Vec3
from Math.Vec4 import Vec4 as Vec4
from Math.Mat4 import Mat4 as Mat4
from Math.Transform import Transform, TransformRotationOrder

orders = ["xyz", "yzx", "zxy", "xzy", "yxz", "zyx"]


class TestTransform(unittest.TestCase):
    def test_ctor(self):
        tx = Transform()
        self.assertAlmostEqual(tx.position.x, 0.0)
        self.assertAlmostEqual(tx.position.y, 0.0)
        self.assertAlmostEqual(tx.position.z, 0.0)
        self.assertAlmostEqual(tx.scale.x, 1.0)
        self.assertAlmostEqual(tx.scale.y, 1.0)
        self.assertAlmostEqual(tx.scale.z, 1.0)
        self.assertAlmostEqual(tx.rotation.x, 0.0)
        self.assertAlmostEqual(tx.rotation.y, 0.0)
        self.assertAlmostEqual(tx.rotation.z, 0.0)

    def test_set_position(self):
        tx = Transform()
        tx.set_position(2.0, 3.5, 4.2)
        self.assertAlmostEqual(tx.position.x, 2.0)
        self.assertAlmostEqual(tx.position.y, 3.5)
        self.assertAlmostEqual(tx.position.z, 4.2)

        tx.set_position(Vec3(2.0, 3.5, 4.2))
        self.assertAlmostEqual(tx.position.x, 2.0)
        self.assertAlmostEqual(tx.position.y, 3.5)
        self.assertAlmostEqual(tx.position.z, 4.2)

        tx.set_position(Vec4(2.0, 3.5, 4.2))
        self.assertAlmostEqual(tx.position.x, 2.0)
        self.assertAlmostEqual(tx.position.y, 3.5)
        self.assertAlmostEqual(tx.position.z, 4.2)

        tx.set_position((2.0, 3.5, 4.2))
        self.assertAlmostEqual(tx.position.x, 2.0)
        self.assertAlmostEqual(tx.position.y, 3.5)
        self.assertAlmostEqual(tx.position.z, 4.2)

        tx.set_position([2.0, 3.5, 4.2])
        self.assertAlmostEqual(tx.position.x, 2.0)
        self.assertAlmostEqual(tx.position.y, 3.5)
        self.assertAlmostEqual(tx.position.z, 4.2)

        with self.assertRaises(ValueError):
            tx.set_position(23, 43, 5, 2)

    def test_set_rotation(self):
        tx = Transform()
        tx.set_rotation(45.0, -20.0, 340)
        self.assertAlmostEqual(tx.rotation.x, 45.0)
        self.assertAlmostEqual(tx.rotation.y, -20.0)
        self.assertAlmostEqual(tx.rotation.z, 340.0)
        tx.set_rotation(Vec3(45.0, -20.0, 340))
        self.assertAlmostEqual(tx.rotation.x, 45.0)
        self.assertAlmostEqual(tx.rotation.y, -20.0)
        self.assertAlmostEqual(tx.rotation.z, 340.0)
        tx.set_rotation(Vec4(45.0, -20.0, 340))
        self.assertAlmostEqual(tx.rotation.x, 45.0)
        self.assertAlmostEqual(tx.rotation.y, -20.0)
        self.assertAlmostEqual(tx.rotation.z, 340.0)

        with self.assertRaises(ValueError):
            tx.set_rotation("hello", 43, 5)

    def test_set_scale(self):
        tx = Transform()
        tx.set_scale(2.0, 5.0, 2.1)
        self.assertAlmostEqual(tx.scale.x, 2.0)
        self.assertAlmostEqual(tx.scale.y, 5.0)
        self.assertAlmostEqual(tx.scale.z, 2.1)
        tx.set_scale(Vec3(2.0, 5.0, 2.1))
        self.assertAlmostEqual(tx.scale.x, 2.0)
        self.assertAlmostEqual(tx.scale.y, 5.0)
        self.assertAlmostEqual(tx.scale.z, 2.1)
        tx.set_scale(Vec4(2.0, 5.0, 2.1))
        self.assertAlmostEqual(tx.scale.x, 2.0)
        self.assertAlmostEqual(tx.scale.y, 5.0)
        self.assertAlmostEqual(tx.scale.z, 2.1)

        with self.assertRaises(ValueError):
            tx.set_scale("hello", 43, 5)

    def test_get_matrix_default(self):

        for o in orders:
            tx = Transform()
            tx.set_order(o)
            matrix = tx.get_matrix()

            # fmt: off
            ident = [1.0, 0.0, 0.0, 0.0,
                    0.0, 1.0, 0.0, 0.0, 
                    0.0, 0.0, 1.0, 0.0,
                    0.0, 0.0, 0.0, 1.0]
            # fmt: on
            self.assertTrue(matrix.get_matrix() == ident)

    def test_set_rotation_order(self):
        tx = Transform()
        for o in orders:
            tx.set_order(o)
            self.assertTrue(tx.order==o)
        with self.assertRaises(TransformRotationOrder):
            tx.set_order("bogus")


    def test_rotation_orders(self) :
        tx = Transform()
        tx.set_rotation(45,25,35)
        tx.set_order("xyz")
        # fmt: off
        result=[0.742404,0.519837,-0.422618,0.0,-0.160787,0.750633,0.640856,0.0,0.650372,-0.407823,0.640856,0.0,0.0,0.0,0.0,1.0]
        # fmt: on

        value=tx.get_matrix().get_matrix()
        print(result,value)

        for r, v in zip(result, value):
            self.assertAlmostEqual(r, v, places=3)
