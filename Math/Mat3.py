"""
Simple Mat3 class which can be used with the Vec3 class
"""

import math
import operator 
import functools

class Mat3Error(Exception):
    """ An exception class for Mat3 """
    pass

class Mat3NotSquare(Exception) :
    """Make sure we have 3x3"""
    pass

class Mat3 :
    __slots__ = ["m"]

    def __init__(self) :
        self.m = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]

    def get_matrix(self) :
        "return matrix as list"
        return functools.reduce(operator.concat, self.m)
    @classmethod
    def identity(cls) :
        "class method to return a new identity matrix"
        v=Mat3()
        return v
        
    @classmethod 
    def zero(cls) :
        "class method to return a zero matrix"
        v=Mat3()
        v.m = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
        return v
    @classmethod
    def from_list(cls,l) :
        "class method to create mat3 from list"
        v=Mat3()        
        v.m=l
        if v._is_square() is not True :
            raise Mat3NotSquare
        else :
            return v    
    
    def _is_square(self) ->bool :
        return len(self.m)==3 and all( len(i)==3 for i in self.m)     

    def transpose(self) :
        "traspose this matrix"
        self.m = [list(item) for item in zip(*self.m)]
    
    def get_transpose(self) :
        m=Mat3()
        m.m=[list(item) for item in zip(*self.m)]
        return m
