import unittest

from Math.Mat3 import Mat3,Mat3NotSquare
import math


class TestMat3(unittest.TestCase):
    def test_ctor(self):
        m = Mat3()
        ident=[1.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0]
        self.assertTrue(m.get_matrix()==ident)

    def test_identity(self) :
        m=Mat3.identity()
        values=m.get_matrix()
        print(values)
        ident=[1.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0]
        self.assertTrue(values==ident)

    def test_zero(self) :
        m=Mat3.zero()
        values=m.get_matrix()
        print(values)
        ident=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        self.assertTrue(values==ident)
    def test_from_list(self) :
        m=Mat3.from_list([[1.0,2.0,3.0],[4.0,5.0,6.0],[7.0,8.0,9.0]])
        result=[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]
        self.assertTrue(m.get_matrix()==result)
    def test_not_square(self) :
        self.assertRaises(Mat3NotSquare,Mat3.from_list,[[1.0,2.0,3.0,50],[4.0,5.0,6.0],[7.0,8.0,9.0]])
        self.assertRaises(Mat3NotSquare,Mat3.from_list,[[],[],[],[]])

    def test_transpose(self) :
        a=Mat3.from_list([[1,2,3],[4,5,6],[7,8,9]])
        a.transpose()
        values=a.get_matrix()
        result=[1,4,7,2,5,8,3,6,9]
        self.assertTrue(values==result)

    def test_get_transpose(self) :
        a=Mat3.from_list([[1,2,3],[4,5,6],[7,8,9]])
        b=a.get_transpose()
        values=b.get_matrix()
        result=[1,4,7,2,5,8,3,6,9]
        self.assertTrue(values==result)

