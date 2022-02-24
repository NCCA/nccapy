from nccapy.Math.Mat4 import Mat4 as Mat4
from nccapy.Math.Vec3 import Vec3 as Vec3
from typing import Any,Union

class Transform:
    position: Vec3
    rotation: Vec3
    scale: Vec3
    matrix: Mat4
    def __init__(self) -> None: ...
    def set_position(self,*args) -> None : ...
    def set_rotation(self,*args) -> None : ...
