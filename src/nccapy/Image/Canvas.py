from typing import Any, Union, Type, Tuple

import pygame
from .Image import Image
class Canvas :
    """
    A class to represent a canvas for interactive rendering of 2D images
    Attributes
    ----------
    width : int
        width of the canvas
    height : int
        height of the canvas
    display : pygame.display
        pygame display object used to render too
    """

    def __init__(self, width : int , height : int ):
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((width, height))

    def set_title(self, title : str) ->None:
        pygame.display.set_caption(title)

    def clear(self, r: int, g: int, b: int, a: int = 255) -> None:
        """
        Sets all pixels to the specified color.

        Parameters
        ----------
            r : int
                red component of the color
            g : int
                green component of the color
            b : int
                blue component of the color
            a : int
                alpha component of the color
        """
        self.display.fill((r, g, b, a))

    def quit(self) -> None:
        pygame.quit()

    def update(self) -> None:
        pygame.display.flip()

    def __enter__(self):
        """Start a timer if using with statement."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()

    def get_event(self) -> Union[Type[pygame.event.Event], Tuple[Type[pygame.event.Event]]] :
        return pygame.event.get()

    def should_quit(self) -> bool:
        for event in self.get_event():
            if event.type == pygame.QUIT:
                return True
        return False

    def put_pixel(self, x: int, y: int, r: int, g: int, b: int, a: int = 255) -> None:
        #self.display.set_at((x, y), (r, g, b, a))
        pixel_array = pygame.PixelArray(self.display)
        pixel_array[x, y] = (r, g, b, a)
        pixel_array.close()
    def put_image(self, image : Image):
        ...