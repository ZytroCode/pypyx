# Importing
import os
import pypyx
import sys

from pypyx.core import config


# Core class
class Core(sys.modules[__name__].__class__):

    # Init function
    @classmethod
    def init(self):
        # Managing configurations
        cfg = dict(config.file)
        DEFAULT = cfg.get("pypyx")
        PYGAME = cfg.get("pygame")
        self.debug = DEFAULT.getboolean("debug")

        self.pygame_support_prompt = PYGAME.getboolean("pygame_support_prompt")
        if not self.pygame_support_prompt:
            os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

        # DEBUG
        if self.debug:
            print(f"[PYX] Debug: {self.debug}")
            print(f"[PYX] Version: {pypyx.__version__}")

        # Initializing
        import pygame

        pygame.init()


Core.init()
sys.modules[__name__].__class__ = Core
