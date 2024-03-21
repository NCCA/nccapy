import pytest

from nccapy.Image import Canvas


def test_ctor():
    canvas = Canvas(128, 128)
    assert canvas.width == 128
    assert canvas.height == 128
    assert canvas.display is not None


def test_set_title():
    canvas = Canvas(128, 128)
    canvas.set_title("test")
    assert canvas.get_title()[0] == "test"


def test_clear():
    canvas = Canvas(128, 128)
    canvas.clear(255, 0, 0, 255)
    assert canvas.display.get_at((0, 0)) == (255, 0, 0, 255)
    canvas.clear(0, 0, 0, 0)
    assert canvas.display.get_at((10, 10)) == (0, 0, 0, 0)


def test_with():
    with Canvas(128, 128) as canvas:
        pass


def test_get_set_pixel():
    canvas = Canvas(128, 128)
    canvas.put_pixel(0, 0, 255, 0, 0)
    assert canvas.display.get_at((0, 0)) == (255, 0, 0, 255)
    canvas.put_pixel(10, 10, 0, 0, 0)
    assert canvas.display.get_at((10, 10)) == (0, 0, 0, 255)
