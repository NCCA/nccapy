import pytest

from nccapy.Image import *


def test_ctor():
    image = Image(128, 128)
    assert image.width == 128
    assert image.height == 128
    assert len(image.pixels) == 128 * 128

def test_clear():
    image = Image(128, 128)
    image.clear(255, 0, 0, 255)
    for pixel in image.pixels:
        r, g, b, a = pixel.get_rgba()
        assert r == 255
        assert g == 0
        assert b == 0
        assert a == 255

def test_save():
    image = Image(128, 128)
    image.clear(255, 0, 0, 255)
    assert image.save("test.png")
    image.clear(255, 0, 0, 255)
    assert image.save("red.png")
    image.clear(0, 255, 0, 255)
    assert image.save("green.png")
    image.clear(0, 0, 255, 255)
    assert image.save("blue.png")

def test_load():
    image = Image(0, 0)
    assert image.load("test.png")
    assert image.width == 128
    assert image.height == 128
    for pixel in image.pixels:
        assert pixel.red() == 255
        assert pixel.green() == 0
        assert pixel.blue() == 0
        assert pixel.alpha() == 255

def test_set_get():
    image = Image(10, 10)
    for x in range(0, 10):
        for y in range(0, 10):
            image.set_pixel(x, y, 128, 255, 64, 255)
    assert image.save("setPixel.png")

    for x in range(0, 10):
        for y in range(0, 10):
            r, g, b, a = image.get_pixel(x, y)
            assert r == 128
            assert g == 255
            assert b == 64
            assert a == 255

def test_get_average_rgba():
    image = Image(20, 20)
    image.clear(255, 0, 0)
    r, g, b, a = image.get_average_rgba()
    assert r == 255
    assert g == 0
    assert b == 0
    assert a == 255

def test_get_average_hsv():
    image = Image(20, 20)
    image.clear(255, 0, 23)
    h, s, v = image.get_average_hsv()
    assert h == 355
    assert s == 100
    assert v == 100
