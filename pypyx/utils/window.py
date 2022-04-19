# Importing
import pygame

from pypyx import SDL2
from typing import Any


class Window(object):
    def __init__(self, **keys) -> None:
        # Setting up display
        self.display = SDL2.Window(resizable=keys.get("resizable", True), hidden=True)
        self.display.title = keys.get("title", "PyPyx Window")
        self.width = keys.get("width", 800)
        self.height = keys.get("height", 600)
        self.display.size = keys.get("size", (self.width, self.height))
        self.display.position = keys.get("position", SDL2.WINDOWPOS_CENTERED)

        if keys.get("visible", True):
            self.display.show()

        # Setting up renderer
        RENDERER_KEYS = dict(
            accelerated=keys.get("accelerated", 1),
            vsync=keys.get("vsync", True),
        )
        self.renderer = SDL2.Renderer(self.display, **RENDERER_KEYS)
        self.renderer.draw_color = (0, 0, 0, 255)

    def fill(self, color: pygame.Color = (0, 0, 0, 255)) -> None:
        self.clear()
        self.renderer.draw_color = (0, 0, 0, 255)

    def clear(self) -> None:
        self.renderer.clear()
