# Importing
from pypyx import SDL2


class Window:
    def __init__(self):
        self.display = SDL2.Window()
        self.renderer = SDL2.Renderer(self.display)
