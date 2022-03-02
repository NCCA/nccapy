import math
import unittest

from Math.Mat4 import Mat4
from Math.Util import clamp, look_at, perspective
from Math.Vec3 import Vec3


class TestUtil(unittest.TestCase):
    def test_clamp(self):
        self.assertEqual(clamp(2, 10, 20), 10)  # test  int up
        self.assertEqual(clamp(200, 10, 20), 20)  # test int down
        self.assertAlmostEqual(clamp(0.1, 0.01, 1.0), 0.1)
        self.assertAlmostEqual(clamp(2.1, 0.01, 1.2), 1.2)

    def test_clamp_error(self):
        self.assertRaises(ValueError, clamp, 1, 100, 0.1)

    def test_look_at(self):
        eye = Vec3(2, 2, 2)
        look = Vec3(0, 0, 0)
        up = Vec3(0, 1, 0)
        view = look_at(eye, look, up)
        # result from Julia function and same as GLM as well
        # fmt: off
        result=[0.7071067811865475, -0.4082482904638631, 0.5773502691896258 ,0.0, 0.0, 0.8164965809277261, 0.5773502691896258, 0.0, -0.7071067811865475, -0.4082482904638631, 0.5773502691896258 ,0.0, -0.0, -0.0, -3.4641016151377553, 1.0]
        # fmt: on
        for r, v in zip(view.get_matrix(), result):
            print(r, v)
            self.assertAlmostEqual(r, v, places=6)

    def test_perspective(self):
        project = perspective(45.0, 1.0, 0.1, 100)
        # fmt: off
        result=[2.4142134189605713, 0.0, 0.0, 0.0, 0.0, 2.4142134189605713, 0.0, 0.0, 0.0, 0.0, -1.0020020008087158, -1.0, 0.0, 0.0, -0.20020020008087158, 0.0]
        result=[2.4142135623730954, 0.0, 0.0, 0.0, 0.0 ,2.4142135623730954, 0.0 ,0.0,0.0 ,0.0, -1.002002002002002, -1.0, 0.0, 0.0, -0.20020020020020018, 0.0]
        # fmt: on
        print(f"Project\n{project.get_matrix()}\nResult\n{result}")
        for r, v in zip(project.get_matrix(), result):
            print(r, v)
            self.assertAlmostEqual(r, v, places=6)
