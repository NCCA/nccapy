import math
import unittest
from Math.Vec3 import Vec3 as Vec3
from Math.Vec4 import Vec4 as Vec4
from Math.Mat4 import Mat4 as Mat4
from Math.Transform import Transform


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
            
    def test_get_matrix(self) :
        tx= Transform()
        matrix=tx.get_matrix()
        print(matrix)