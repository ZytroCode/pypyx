"""PyPyx is a python library used for making games with the help of pygame.

PyPyx is a 3rd party open-source python library that unlocks the potential of your games.
With PyPyx's features, the limits of your games are unlimited.
"""

# Configs
__version__ = "0.2.3"
__author__ = "ZytroCode"
__all__ = [
    "Rect",
    "Ellipse",
    "Window",
    "Color",
]

# Core
from pypyx import core

# Tools
from pygame import _sdl2 as SDL2
from pygame import Color
from pypyx import entity
from pypyx import utils
from pypyx.entity import *
from pypyx.utils import *
