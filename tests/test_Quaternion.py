import pytest
from nccapy.Math.Quaternion import Quaternion
from nccapy.Math.Mat4 import Mat4


def test_Quaternion():
    q = Quaternion()
    assert q.s == 1.0
    assert q.x == 0.0
    assert q.y == 0.0
    assert q.z == 0.0
    q = Quaternion(0.2, 0.0, 1.0, 0.0)
    assert q.s == 0.2
    assert q.x == 0.0
    assert q.y == 1.0
    assert q.z == 0.0


def test_from_mat4():
    test = Quaternion.from_mat4(Mat4.rotateX(45.0))
    assert test.s == pytest.approx(0.92388, rel=1e-3)
    assert test.x == pytest.approx(0.38268, rel=1e-3)
    assert test.y == pytest.approx(0.0)
    assert test.z == pytest.approx(0.0)
    test = Quaternion.from_mat4(Mat4.rotateY(45.0))
    assert test.s == pytest.approx(0.92388, rel=1e-3)
    assert test.x == pytest.approx(0.0)
    assert test.y == pytest.approx(0.38268, rel=1e-3)
    assert test.z == pytest.approx(0.0)
    test = Quaternion.from_mat4(Mat4.rotateZ(45.0))
    assert test.s == pytest.approx(0.92388, rel=1e-3)
    assert test.x == pytest.approx(0.0)
    assert test.y == pytest.approx(0.0)
    assert test.z == pytest.approx(0.38268, rel=1e-3)


def test_addition():
    a = Quaternion(0.5, 1.0, 0.0, 0.0)
    b = Quaternion(0.2, 0.0, 1.0, 0.0)
    c = a + b
    assert c.s == 0.7
    assert c.x == 1.0
    assert c.y == 1.0
    assert c.z == 0.0
