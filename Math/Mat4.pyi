from typing import Any,Union
from Math.Vec4 import Vec4
class Mat4Error(Exception): ...
class Mat4NotSquare(Exception): ...

class Mat4:
    m: Any
    def __init__(self) -> None: ...
    def get_matrix(self): ...
    @classmethod
    def identity(cls): ...
    @classmethod
    def zero(cls): ...
    @classmethod
    def from_list(cls, l): ...
    def transpose(self) -> None: ...
    def get_transpose(self): ...
    def scale(self, x: float, y: float, z: float): ...
    def rotateX(self, angle) -> None: ...
    def rotateY(self, angle) -> None: ...
    def rotateZ(self, angle) -> None: ...
    def __getitem__(self, idx): ...
    def __setitem__(self, idx, item) -> float: ...
    def __mul__(self, rhs : Union[float,int]) ->Mat4 : ...
    def __matmul__(self, rhs : Union[Vec4,Mat4])-> Union[Mat4,Vec4]: ...
    def __imul__(self, rhs : Union[float,int])-> Union[Mat4,Vec4]: ...
