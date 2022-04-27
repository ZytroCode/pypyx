# Importing
import pygame

from pypyx import SDL2
from typing import Any


class Sprite:
    __dict__ = {}
    getters = {
        "position": lambda self: (self.x, self.y),
        "pos": lambda self: (self.x, self.y),
    }

    def __init__(
        self,
        path: str,
        x: int,
        y: int,
        angle: int = 0,
    ):
        self.path = path
        self.x = x
        self.y = y
        self.angle = angle

    def __getattr__(self, name: str) -> Any:
        try:
            if name in self.getters.keys():
                return self.getters[name](self)
            return self.__dict__[name]
        except KeyError as e:
            error = AttributeError(f"'{self.__class__.__name__}' object has no attribute {name}")
            raise error

    def __setattr__(self, name: str, value: Any) -> None:
        if name == "position":
            self.__dict__["x"] = value[0]
            self.__dict__["y"] = value[1]
        elif name == "pos":
            self.__dict__["x"] = value[0]
            self.__dict__["y"] = value[1]
        else:
            self.__dict__[name] = value

    def __draw__(self, renderer: SDL2.Renderer) -> SDL2.Image:
        image = pygame.image.load(self.path)
        image = pygame.transform.rotate(image, self.angle)
        image = SDL2.Texture.from_surface(renderer, image)
        return SDL2.Image(image)
