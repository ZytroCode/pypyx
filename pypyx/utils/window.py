# Importing
import pygame

from pypyx import SDL2
from typing import Any


        self.renderer = SDL2.Renderer(self.display)
class Window(object):
    def __init__(self, **keys) -> None:
        # Setting up display
        self.display = SDL2.Window(resizable=keys.get("resizable", True), hidden=True)
        self.display.title = keys.get("title", "PyPyx Window")
        self.width = keys.get("width", 800)
        self.height = keys.get("height", 600)
        self.display.size = keys.get("size", (self.width, self.height))
        self.display.position = keys.get("position", SDL2.WINDOWPOS_CENTERED)
