from typing import Any, Union

from Math.Mat3 import Mat3

class Vec3:
    x: float
    y: float
    z: float
    def __init__(self, x: float = ..., y: float = ..., z: float = ...) -> None: ...
    def __add__(self, rhs: Vec3) -> Vec3: ...
    def __iadd__(self, rhs: Vec3) -> Vec3: ...
    def __sub__(self, rhs: Vec3) -> Vec3: ...
    def __isub__(self, rhs: Vec3) -> Vec3: ...
    def __eq__(self, rhs: object) -> bool: ...
    def __neq__(self, rhs: object) -> bool: ...
    def __neg__(self) -> Vec3: ...
    def set(self, x: float, y: float, z: float): ...
    def dot(self, rhs: Vec3) -> float: ...
    def length(self) -> float: ...
    def length_squared(self) -> float: ...
    def inner(self, rhs: Vec3) -> float: ...
    def null(self) -> None: ...
    def cross(self, rhs: Vec3) -> Vec3: ...
    def normalize(self) -> None: ...
    def reflect(self, n: Vec3) -> Vec3: ...
    def clamp(self, low: float, high: float): ...
    def outer(self, rhs: Vec3) -> Mat3: ...
    def __mul__(self, rhs: Union[float, int]) -> Vec3: ...
    def __rmul__(self, rhs: Union[float, int]) -> Vec3: ...
    def __matmul__(self, rhs: Mat3) -> Vec3: ...
