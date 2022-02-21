import math
import unittest
from Math.Mat3 import Mat3, Mat3NotSquare
from Math.Vec3 import Vec3


class TestMat3(unittest.TestCase):
    def test_ctor(self):
        m = Mat3()
        ident = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        self.assertTrue(m.get_matrix() == ident)

    def test_identity(self):
        m = Mat3.identity()
        values = m.get_matrix()
        print(values)
        ident = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        self.assertTrue(values == ident)

    def test_zero(self):
        m = Mat3.zero()
        values = m.get_matrix()
        print(values)
        ident = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.assertTrue(values == ident)

    def test_from_list(self):
        m = Mat3.from_list([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
        result = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
        self.assertTrue(m.get_matrix() == result)

    def test_not_square(self):
        self.assertRaises(
            Mat3NotSquare,
            Mat3.from_list,
            [[1.0, 2.0, 3.0, 50], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]],
        )
        self.assertRaises(Mat3NotSquare, Mat3.from_list, [[], [], [], []])

    def test_transpose(self):
        a = Mat3.from_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        a.transpose()
        values = a.get_matrix()
        result = [1, 4, 7, 2, 5, 8, 3, 6, 9]
        self.assertTrue(values == result)

    def test_get_transpose(self):
        a = Mat3.from_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        b = a.get_transpose()
        values = b.get_matrix()
        result = [1, 4, 7, 2, 5, 8, 3, 6, 9]
        self.assertTrue(values == result)

    def test_scale(self):
        a = Mat3()
        a.scale(2.0, 3.0, 4.0)
        value = a.get_matrix()
        result = [2.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 4.0]
        self.assertTrue(value == result)

    def test_rotateX(self):
        a = Mat3()
        a.rotateX(45.0)
        value = a.get_matrix()
        result = [1.0, 0.0, 0.0, 0.0, 0.707107, 0.707107, 0.0, -0.707107, 0.707107]
        for r, v in zip(result, value):
            self.assertAlmostEqual(r, v, places=6)

    def test_rotateY(self):
        a = Mat3()
        a.rotateY(25.0)
        value = a.get_matrix()
        result = [0.906308, 0.0, -0.422618, 0.0, 1.0, 0.0, 0.422618, 0.0, 0.906308]
        for r, v in zip(result, value):
            self.assertAlmostEqual(r, v, places=6)

    def test_rotateZ(self):
        a = Mat3()
        a.rotateZ(-36.0)
        value = a.get_matrix()
        result = [0.809017, -0.587785, 0.0, 0.587785, 0.809017, 0.0, 0.0, 0.0, 1.0]
        for r, v in zip(result, value):
            self.assertAlmostEqual(r, v, places=6)

    def test_mult_mat3_mat3(self):
        t1 = Mat3()
        t2 = Mat3()
        t1.rotateX(45.0)
        t2.rotateY(35.0)
        test = t1 * t2
        # fmt: off
        result = [0.819152,0.0,-0.573577,0.40558,0.707107,0.579228,0.40558,-0.707107,0.579228]
        # fmt: on
        value = test.get_matrix()
        for r, v in zip(result, value):
            self.assertAlmostEqual(r, v, places=4)

        test = t1 @ t2
        value = test.get_matrix()
        for r, v in zip(result, value):
            self.assertAlmostEqual(r, v, places=4)

    def test_mult_mat3_equal(self):
        t1 = Mat3()
        t2 = Mat3()
        t1.rotateX(45.0)
        t2.rotateY(35.0)
        t1 *= t2
        # fmt: off
        result = [0.819152,0.0,-0.573577,0.40558,0.707107,0.579228,0.40558,-0.707107,0.579228]
        # fmt: on
        value = t1.get_matrix()
        for r, v in zip(result, value):
            self.assertAlmostEqual(r, v, places=4)

        t1.rotateX(45.0)
        t1 @= t2
        value = t1.get_matrix()
        for r, v in zip(result, value):
            self.assertAlmostEqual(r, v, places=4)

    def test_mat3_mult_vec3(self):
        t1 = Mat3()
        test = Vec3(2.0, 1.0, 2.0)
        t1.rotateX(45.0)
        test = test * t1
        self.assertAlmostEqual(test.x, 2.0, places=6)
        self.assertAlmostEqual(test.y, -0.707107, places=6)
        self.assertAlmostEqual(test.z, 2.12132, places=6)
