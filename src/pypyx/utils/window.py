# Importing
import pygame

from pypyx import core
from pypyx import SDL2
from typing import Any


class Window:
    __dict__ = {}
    getters = {
        "events": lambda self: [
            event
            for event in self._events
            if getattr(event, "window", None) is not None
            if setattr(event, "name", pygame.event.event_name(event.type)) is None
        ],

        "title": lambda self: self.display.title,
        "size": lambda self: self.display.size,
        "width": lambda self: self.size[0],
        "height": lambda self: self.size[1],
        "position": lambda self: self.display.position,
        "pos": lambda self: self.position,
        "x": lambda self: self.pos[0],
        "y": lambda self: self.pos[1],
        "center": lambda self: (self.width/2, self.height/2),
        "resizable": lambda self: self.display.resizable,
    }

    def __init__(self, **keys) -> None:
        # Setting up display
        self.display = SDL2.Window(hidden=True)
        self.title = keys.get("title", "PyPyx Window")
        self.size = keys.get("size", (800, 600))
        self.width = keys.get("width", 800)
        self.height = keys.get("height", 600)
        self.position = keys.get("position", SDL2.WINDOWPOS_CENTERED)
        self.resizable = keys.get("resizable", True)
        self.visible = keys.get("visible", True)

        # Setting up renderer
        try:
            self.renderer = SDL2.Renderer(
                self.display,
                accelerated=keys.get("accelerated", 1),
                vsync=keys.get("vsync", True),
            )
        except SDL2.sdl2.error:
            core.vsync_available = False
            if core.debug:
                print("[PYX] Vsync is not supported for your display")
            self.renderer = SDL2.Renderer(
                self.display,
                accelerated=keys.get("accelerated", 1),
                vsync=False,
            )
        else:
            core.vsync_available = True
        self.clear()
        self.update()

    def __getattr__(self, name: str) -> Any:
        try:
            if name in self.getters.keys():
                return self.getters[name](self)
            return self.__dict__[name]
        except KeyError as e:
            error = AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
            raise error

    def __setattr__(self, name: str, value: Any) -> None:
        if name == "title":
            self.display.title = value
        elif name == "size":
            self.display.size = value
        elif name == "width":
            self.size = (value, self.size[1])
        elif name == "height":
            self.size = (self.size[0], value)
        elif name == "position":
            self.display.position = value
        elif name == "pos":
            self.position = value
        elif name == "x":
            self.pos = (value, self.pos[1])
        elif name == "y":
            self.pos = (self.pos[0], value)
        elif name == "center":
            self.size = (value[0]*2, value[1]*2)
        elif name == "resizable":
            self.display.resizable = value
        elif name == "visible":
            if value:
                self.display.show()
            else:
                self.display.hide()
        else:
            self.__dict__[name] = value


    def fill(self, color: pygame.Color = (20, 20, 20, 255)) -> None:
        self.renderer.target = None
        self.renderer.draw_color = color
        self.clear()

    def clear(self) -> None:
        self.renderer.clear()

    def update(self) -> None:
        self.renderer.present()
        self._events = pygame.event.get()
