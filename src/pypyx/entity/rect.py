# Importing
import pygame

from pypyx import SDL2
from typing import Any


class Rect:
    __dict__ = {}
    getters = {
        "position": lambda self: (self.x, self.y),
        "pos": lambda self: (self.x, self.y),
        "center": lambda self: (self.x, self.y),
        "top": lambda self: self.y - self.height/2,
        "bottom": lambda self: self.y + self.height/2,
        "left": lambda self: self.x - self.width/2,
        "right": lambda self: self.x + self.width/2,
        "size": lambda self: (self.width, self.height),
        "w": lambda self: self.width,
        "h": lambda self: self.height,
    }

    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        color: pygame.Color = (255, 255, 255),
        angle: int = 0
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
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
        elif name == "center":
            self.__dict__["x"] = value[0]
            self.__dict__["y"] = value[1]
        elif name == "top":
            self.__dict__["y"] = value - self.height/2
        elif name == "bottom":
            self.__dict__["y"] = value + self.height/2
        elif name == "left":
            self.__dict__["x"] = value + self.width/2
        elif name == "right":
            self.__dict__["x"] = value - self.width/2
        elif name == "size":
            self.__dict__["width"] = value[0]
            self.__dict__["height"] = value[1]
        elif name == "w":
            self.__dict__["width"] = value
        elif name == "h":
            self.__dict__["height"] = value
        else:
            self.__dict__[name] = value

    def __draw__(self, renderer: SDL2.Renderer) -> None:
        image = pygame.Surface(self.size)
        image.fill(self.color)
        image = pygame.transform.rotate(image, self.angle)
        image = SDL2.Texture.from_surface(renderer, image)
        return SDL2.Image(image)
