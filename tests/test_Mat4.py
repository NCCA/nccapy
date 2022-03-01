import math
import unittest
from Math.Mat4 import Mat4, Mat4NotSquare, Mat4Error
from Math.Vec4 import Vec4
import tests.mat4Data  as mat4Data # this is generated from the julia file gen_mat4_tests.jl



class TestMat4(unittest.TestCase):

    def compare_matrix(self,a,b,places=6) :
        for r, v in zip(a, b):
            self.assertAlmostEqual(r, v, places=places)


    def test_ctor(self):
        m = Mat4()
        # fmt: off
        ident = [1.0, 0.0, 0.0, 0.0,
                 0.0, 1.0, 0.0, 0.0, 
                 0.0, 0.0, 1.0, 0.0,
                 0.0, 0.0, 0.0, 1.0]
        # fmt: on
        self.compare_matrix(ident,m.get_matrix())
    def test_identity(self):
        m = Mat4.identity()
        # fmt: off
        ident = [1.0, 0.0, 0.0, 0.0,
                 0.0, 1.0, 0.0, 0.0, 
                 0.0, 0.0, 1.0, 0.0,
                 0.0, 0.0, 0.0, 1.0]
        # fmt: on
        self.compare_matrix(ident,m.get_matrix())

    def test_zero(self):
        m = Mat4.zero()
        values = m.get_matrix()
        ident = [0.0] * 16
        self.compare_matrix(ident,values)

    def test_from_list(self):
        m = Mat4.from_list(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        )
        result = [i for i in range(1, 17)]
        self.compare_matrix(m.get_matrix(), result)
        m = Mat4.from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        self.compare_matrix(m.get_matrix(), result)

    def test_not_square(self):
        with self.assertRaises(Mat4NotSquare):
            _ = Mat4.from_list([[1.0, 2.0, 3.0, 50], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
        with self.assertRaises(Mat4NotSquare):
            _ = Mat4.from_list([[], [], [], []])

    def test_transpose(self):
        m = Mat4.from_list(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        )
        m.transpose()
        values = m.get_matrix()
        result = [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]
        self.compare_matrix(values, result)

    def test_get_transpose(self):
        m = Mat4.from_list(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        )
        b = m.get_transpose()
        values = b.get_matrix()
        result = [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]
        self.compare_matrix(values, result)

    def test_scale(self):
        a= Mat4.scale(2.0, 3.0, 4.0)
        value = a.get_matrix()
        # fmt: off
        result = [2.0,0.0,0.0,0.0,0.0,3.0,0.0,0.0,0.0,0.0,4.0,0.0,0.0,0.0,0.0,1.0]
        # fmt: on
        self.compare_matrix(value, result)

    def test_rotateX(self):
        a = Mat4.rotateX(45.0)
        value = a.get_matrix()
        # fmt: off
        result = [1.0,0.0,0.0,0.0,
                    0.0,0.707107,0.707107,0.0,
                    0.0,-0.707107,0.707107,0.0,
                    0.0,0.0,0.0,1.0]

        # fmt: on
        self.compare_matrix(value, result)

    def test_rotateY(self):
        a=Mat4.rotateY(25.0)
        value = a.get_matrix()
        # fmt: off
        result = [0.906308,0.0,-0.422618,0.0,
                  0.0,1.0,0.0,0.0,
                  0.422618,0.0,0.906308,0.0,
                  0.0,0.0,0.0,1.0]
    
        print(result)
        # fmt: on
        self.compare_matrix(value, result)

    def test_rotateZ(self):
        a=Mat4.rotateZ(-36.0)
        value = a.get_matrix()
        # fmt: off
        result = [0.809,-0.5877,0.0,0.0,
                  0.5877, 0.809, 0.0, 0.0,
                  0.0,0.0,1.0, 0.0,  
                  0.0, 0.0,0.0,1.0,]
        # fmt: on
        self.compare_matrix(value, result,places=3)

    def test_mat4_times_mat4(self) :
        for a,b,result in zip(mat4Data.a,mat4Data.b,mat4Data.a_times_b) :
            m1=Mat4.from_list(a)
            m2=Mat4.from_list(b)
            print(type(m1.m),len(m1.m))
            print(m1)
            value=m1@m2
            self.compare_matrix(value.get_matrix(), result)


    def test_rotate_mat4_mat4(self):
        t1=Mat4.rotateX(45.0)
        t2=Mat4.rotateY(35.0)
        test = t1 @ t2
        # fmt: off
        result=[0.819152,0.405580,-0.405580,0.0,
                0.0,0.707107,0.707107,0.0,
                0.573577,-0.579228,0.579228,0.0,
                0.0,0.0,0.0,1.0]
        # fmt: on
        value = test.get_matrix()
        self.compare_matrix(value, result,places=4)

        test = t1 @ t2
        value = test.get_matrix()
        self.compare_matrix(value, result,places=4)

    def test_mult_error(self):
        with self.assertRaises(Mat4Error):
            a = Mat4()
            c = a @ 2

    def test_mult_mat4_equal(self):
        for a,b,result in zip(mat4Data.a,mat4Data.b,mat4Data.a_times_b) :
            m1=Mat4.from_list(a)
            m2=Mat4.from_list(b)
            m1@=m2
            self.compare_matrix(m1.get_matrix(), result)

    def test_mat4_mult_vec4(self):
        test = Vec4(1.0, 2.0, 3.0, 1.0)
        t1=Mat4.rotateX(45.0)
        test = t1 @ test
        self.assertAlmostEqual(test.x, 1.0, places=5)
        self.assertAlmostEqual(test.y, 3.535534, places=5)
        self.assertAlmostEqual(test.z, 0.707107, places=5)
        self.assertAlmostEqual(test.w, 1.0, places=5)


    def test_mat4_plus_mat4(self) :
        for a,b,result in zip(mat4Data.a,mat4Data.b,mat4Data.a_plus_b) :
            m1=Mat4.from_list(a)
            m2=Mat4.from_list(b)
            values=m1+m2
            self.compare_matrix(values.get_matrix(), result)

    def test_mat4_plus_equal(self) :
        for a,b,result in zip(mat4Data.a,mat4Data.b,mat4Data.a_plus_b) :
            m1=Mat4.from_list(a)
            m2=Mat4.from_list(b)
            m1+=m2
            self.compare_matrix(m1.get_matrix(), result)
   
    def test_mat4_minus_mat4(self) :
        for a,b,result in zip(mat4Data.a,mat4Data.b,mat4Data.a_minus_b) :
            m1=Mat4.from_list(a)
            m2=Mat4.from_list(b)
            values=m1-m2
            self.compare_matrix(values.get_matrix(), result)

    def test_mat4_minus_equal(self) :
        for a,b,result in zip(mat4Data.a,mat4Data.b,mat4Data.a_minus_b) :
            m1=Mat4.from_list(a)
            m2=Mat4.from_list(b)
            m1-=m2
            self.compare_matrix(m1.get_matrix(), result)
