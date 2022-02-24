"""
Class to represent a transform using translate, rotate and scale, 
"""

import math
from nccapy.Math.Mat4 import Mat4
from nccapy.Math.Vec3 import Vec3
from nccapy.Math.Vec4 import Vec4


class TransformRotationOrder(Exception):
    pass


class Transform:
    position = Vec3(0.0, 0.0, 0.0)
    rotation = Vec3(0.0, 0.0, 0.0)
    scale = Vec3(1.0, 1.0, 1.0)
    matrix = Mat4()
    order = "xyz"
    rot_order = {
        "xyz": "rz@ry@rx",
        "yzx": "rx@rz@ry",
        "zxy": "ry@rx@rz",
        "xzy": "ry@rz@rx",
        "yxz": "rz@rx@ry",
        "zyx": "rx@ry@rz",
    }

    def __init__(self):
        pass

    def _set_value(self, args):
        v = Vec3()

        if len(args) == 1:  # one argument
            if isinstance(args[0], (list, tuple)):
                v.x = args[0][0]
                v.y = args[0][1]
                v.z = args[0][2]
            else:  # try vec types
                v.x = args[0].x
                v.y = args[0].y
                v.z = args[0].z
            return v
        elif len(args) == 3:  # 3 as x,y,z
            v.x = float(args[0])
            v.y = float(args[1])
            v.z = float(args[2])
            return v
        else:
            raise ValueError

    def set_position(self, *args):
        self.position = self._set_value(args)

    def set_rotation(self, *args):
        self.rotation = self._set_value(args)

    def set_scale(self, *args):
        self.scale = self._set_value(args)

    def set_order(self, order):
        if order not in self.rot_order:
            raise TransformRotationOrder
        self.order = order

    def get_matrix(self):
        scale = Mat4()
        rx = Mat4()
        ry = Mat4()
        rz = Mat4()
        trans = Mat4()
        scale.scale(self.scale.x, self.scale.y, self.scale.z)
        rx.rotateX(self.rotation.x)
        ry.rotateY(self.rotation.y)
        rz.rotateZ(self.rotation.z)
        rotationScale = eval(self.rot_order.get(self.order)) @ scale
        print("eval\n {}\n".format(eval(self.rot_order.get(self.order))))
        self.matrix = rotationScale
        self.matrix.m[3][0] = self.position.x
        self.matrix.m[3][1] = self.position.y
        self.matrix.m[3][2] = self.position.z
        self.matrix.m[3][3] = 1.0
        return self.matrix

    def __str__(self):
        return f"pos {self.position}\nrot {self.rotation}\nscale {self.scale}"
