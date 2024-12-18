from typing import Union


class Vec4:
    x: float
    y: float
    z: float
    w: float
    def __init__(self, x: float = ..., y: float = ..., z: float = ..., w: float = ...) -> None: ...
    def __add__(self, rhs: Vec4) -> Vec4: ...
    def __iadd__(self, rhs: Vec4) -> Vec4: ...
    def __sub__(self, rhs: Vec4) -> Vec4: ...
    def __isub__(self, rhs: Vec4) -> Vec4: ...
    def set(self, x: float, y: float, z: float, w: float = ...): ...
    def dot(self, rhs: Vec4) -> float: ...
    def length(self) -> float: ...
    def length_squared(self) -> float: ...
    def normalize(self) -> None: ...
    def __eq__(self, rhs: object) -> bool: ...
    def __neq__(self, rhs: object) -> bool: ...
    def __neg__(self) -> Vec4: ...
    def __mul__(self, rhs: Union[float, int]) -> Vec4: ...
    def __rmul__(self, rhs: Union[float, int]) -> Vec4: ...
