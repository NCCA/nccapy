from io import BytesIO
from typing import Tuple

import PIL.Image
from typing_extensions import Self

from .RGBA import RGBA


class Image:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pixels = list()
        for i in range(width * height):
            self.pixels.append(RGBA())

    def clear(self, r: int, g: int, b: int, a: int = 255):
        for pixel in self.pixels:
            pixel.set(r, g, b, a)

    def save(self, filename: str) -> bool:
        # build image buffer
        buffer = list()
        for pixel in self.pixels:
            buffer.append(pixel.pixel)
        image = PIL.Image.new("RGBA", (self.width, self.height), "white")
        image.putdata(buffer)

        try:
            image.save(filename)
        except IOError:
            return False
        return True

    def load(self, filename: str) -> bool:
        try:
            with PIL.Image.open(filename) as im:
                self.width = im.size[0]
                self.height = im.size[1]
                # remove old pixels if there
                self.pixels = list()
                for pixel in im.getdata():
                    self.pixels.append(
                        RGBA(pixel[0], pixel[1], pixel[2], pixel[3])
                    )

        except IOError:
            return False
        return True

    def set_pixel(self, x: int, y: int, r: int, g: int, b: int, a: int = 255) -> None:
        offset = (y * self.width) + x
        try:
            self.pixels[offset].set(r, g, b, a)
        except IndexError:
            # print(f"error out of bounds for {x=} {y=}")
            pass

    def get_pixel(self, x: int, y: int) -> Tuple[int, int, int, int]:
        offset = (y * self.width) + x
        try:
            pixel = self.pixels[offset]
            return pixel.red(), pixel.green(), pixel.blue(), pixel.alpha()
        except IndexError:
            # print(f"error out of bounds for {x=} {y=}")
            pass

    def get_average_rgba(self):
        average_pixel = int(sum(x.pixel for x in self.pixels) / len(self.pixels))
        new_pixel = RGBA.from_pixel(average_pixel)
        r = new_pixel.red()
        g = new_pixel.green()
        b = new_pixel.blue()
        a = new_pixel.alpha()
        return r, g, b, a

    def get_average_hsv(self):
        average_pixel = int(sum(x.pixel for x in self.pixels) / len(self.pixels))

        new_pixel = RGBA.from_pixel(average_pixel)
        h, s, v = new_pixel.as_hsv()
        return h, s, v
