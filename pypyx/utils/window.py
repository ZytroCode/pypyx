# Importing
import pygame

from pypyx import SDL2
from typing import Any


class Window(object):
    def __init__(self, **keys) -> None:
        # Setting up display
        self.display = SDL2.Window(hidden=True)
        self.title = keys.get("title", "PyPyx Window")
        self.size = keys.get("size", (800, 600))
        self.width = keys.get("width", 800)
        self.height = keys.get("height", 600)
        self.position = keys.get("position", SDL2.WINDOWPOS_CENTERED)
        self.visible = keys.get("visible", True)
        self.resizable = keys.get("resizable", True)

        # Setting up renderer
        self.renderer = SDL2.Renderer(
            self.display,
            accelerated=keys.get("accelerated", 1),
            vsync=keys.get("vsync", True),
        )
        self.clear()
        self.update()

    def __getattr__(self, name: str) -> Any:
        if name == "events":
            return [event for event in self._events if getattr(event, "window", None) is not None]

        try:
            super().__getattr__(name)
        except AttributeError:
            error = AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
            raise error

    def __setattr__(self, name: str, value: Any) -> None:
        if name == "display":
            pass
        elif name == "title":
            self.display.title = value
        elif name == "width":
            self.size = (value, self.size[1])
        elif name == "height":
            self.size = (self.size[0], value)
        elif name == "size":
            self.display.size = value
        elif name == "x":
            self.pos = (value, self.pos[1])
        elif name == "y":
            self.pos = (self.pos[0], value)
        elif name in ["pos", "position"]:
            self.display.position = value
        elif name == "visible":
            if value:
                self.display.show()
            else:
                self.display.hide()
        elif name == "resizable":
            self.display.resizable = True

        super().__setattr__(name, value)

    def fill(self, color: pygame.Color = (20, 20, 20, 255)) -> None:
        self.renderer.target = None
        self.renderer.draw_color = color
        self.clear()

    def clear(self) -> None:
        self.renderer.clear()

    def update(self) -> None:
        self.renderer.present()
        self._events = pygame.event.get()
