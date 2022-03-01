import math
import unittest
from Math.Mat3 import Mat3, Mat3NotSquare, Mat3Error
from Math.Vec3 import Vec3
import tests.mat3Data  as mat3Data # this is generated from the julia file gen_mat4_tests.jl


class TestMat3(unittest.TestCase):
    def compare_matrix(self,a,b,places=6) :
        for r, v in zip(a, b):
            self.assertAlmostEqual(r, v, places=places)

    def test_ctor(self):
        m = Mat3()
        ident = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        self.compare_matrix(m.get_matrix(),ident)

    def test_identity(self):
        m = Mat3.identity()
        values = m.get_matrix()
        ident = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        self.compare_matrix(values,ident)
        
    def test_zero(self):
        m = Mat3.zero()
        values = m.get_matrix()
        ident = [0.0] * 9
        self.compare_matrix(values,ident)

    def test_from_list(self):
        m = Mat3.from_list([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
        result = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
        self.compare_matrix(m.get_matrix(),result)
        m = Mat3.from_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.compare_matrix(m.get_matrix(),result)

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
        self.compare_matrix(values,result)

    def test_get_transpose(self):
        a = Mat3.from_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        b = a.get_transpose()
        values = b.get_matrix()
        result = [1, 4, 7, 2, 5, 8, 3, 6, 9]
        self.compare_matrix(values,result)

    def test_scale(self):
        
        a=Mat3.scale(2.0, 3.0, 4.0)
        values = a.get_matrix()
        result = [2.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 4.0]
        self.compare_matrix(values,result)

    def test_rotateX(self):
        a=Mat3.rotateX(45.0)
        values = a.get_matrix()
        result = [1.0, 0.0, 0.0, 0.0, 0.707107, 0.707107, 0.0, -0.707107, 0.707107]
        self.compare_matrix(values,result)

    def test_rotateY(self):
        
        a=Mat3.rotateY(25.0)
        values = a.get_matrix()
        result = [0.906308, 0.0, -0.422618, 0.0, 1.0, 0.0, 0.422618, 0.0, 0.906308]
        self.compare_matrix(values,result)

    def test_rotateZ(self):
        a=Mat3.rotateZ(-36.0)
        values = a.get_matrix()
        result = [0.809017, -0.587785, 0.0, 0.587785, 0.809017, 0.0, 0.0, 0.0, 1.0]
        self.compare_matrix(values,result)




    def test_mult_mat3_mat3(self):
        t1=Mat3.rotateX(45.0)
        t2=Mat3.rotateY(35.0)
        test = t1 @ t2
        # fmt: off
        result = [0.8191, 0.4055, -0.405,0.0, 0.707, 0.707,0.5735, -0.5792, 0.5792]
        # fmt: on
        values = test.get_matrix()
        self.compare_matrix(values,result,places=2)

        t1=Mat3.from_list([1,2,3,2,3,4,4,5,6])
        test=t1@t1
        values = test.get_matrix()
        result=[17, 23, 29,24, 33, 42,38, 53, 68]
        self.compare_matrix(values,result,places=2)

        

    def test_mult_error(self):
        with self.assertRaises(Mat3Error):
            a = Mat3()
            c = a @ 2

    def test_mat3_times_mat3(self) :
        for a,b,result in zip(mat3Data.a,mat3Data.b,mat3Data.a_times_b) :
            m1=Mat3.from_list(a)
            m2=Mat3.from_list(b)
            value=m1@m2
            self.compare_matrix(value.get_matrix(), result)


    def test_mult_mat3_equal(self):
        for a,b,result in zip(mat3Data.a,mat3Data.b,mat3Data.a_times_b) :
            m1=Mat3.from_list(a)
            m2=Mat3.from_list(b)
            m1@=m2
            self.compare_matrix(m1.get_matrix(), result)

    # def test_mult_mat3_equal(self):
    #     t1=Mat3.rotateX(45.0)
    #     t2=Mat3.rotateY(35.0)
    #     t1 @=t2
    #     # fmt: off
    #     result = [0.81915, 0.0, -0.5735, 0.40557, 0.707, 0.57922, 0.40557, -0.7071, 0.5792]
    #     # fmt: on
    #     values = t1.get_matrix()
    #     self.compare_matrix(values,result,places=2)

    def test_mat3_mult_vec3(self):
        t1 = Mat3()
        v1 = Vec3(1.0, 2.0, 3.0)
        t1.rotateX(45.0)
        result = t1 @ v1
        self.assertAlmostEqual(result.x, 1.0, places=4)
        self.assertAlmostEqual(result.y, 3.535534, places=5)
        self.assertAlmostEqual(result.z, 0.707107, places=5)

    def test_add(self):
        a = Mat3.from_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        b = Mat3.from_list([[2, 2, 2], [3, 3, 3], [4, 4, 4]])
        c = a + b
        result = c.get_matrix()
        value = [3, 4, 5, 7, 8, 9, 11, 12, 13]
        for r, v in zip(result, value):
            self.assertAlmostEqual(r, v, places=4)

    def test_plus_equals(self):
        a = Mat3.from_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        b = Mat3.from_list([[2, 2, 2], [3, 3, 3], [4, 4, 4]])
        a += b
        result = a.get_matrix()
        value = [3, 4, 5, 7, 8, 9, 11, 12, 13]
        for r, v in zip(result, value):
            self.assertAlmostEqual(r, v, places=4)

    def test_determinant(self):
        a = Mat3.from_list([[1, 0, 0], [0, 2, 2], [0, -0.5, 2]])
        self.assertAlmostEqual(a.determinant(), 5.0)

    def test_inverse(self):
        test = Mat3.from_list([[1, 0, 0], [0, 2, 2], [0, -0.5, 2]])
        test = test.inverse()
        value = test.get_matrix()
        result = [1.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.0, -0.4, 0.4]
        for r, v in zip(result, value):
            self.assertAlmostEqual(r, v, places=6)
