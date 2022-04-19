# Importing
import pygame

from pypyx import SDL2
from typing import Any


class Window:
    def __init__(self):
        self.display = SDL2.Window()
        self.renderer = SDL2.Renderer(self.display)
