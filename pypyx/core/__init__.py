# Importing
import os
import pypyx
import sys

from configparser import ConfigParser


class Core(sys.modules[__name__].__class__):
    config = ConfigParser()
    config.read([
        f"{os.getcwd()}\\pypyx.ini",  # Custom configuration by user
        f"{os.path.dirname(__file__)}\\pypyx.ini",  # Default configuration
    ])

    @classmethod
    def init(self):
        # Managing configurations
        file = f"{os.path.dirname(__file__)}\\pypyx.ini"
        raise Exception(f"{file} {os.path.exists(file)}")
        PYPYX = self.config["pypyx"]
        PYGAME = self.config["pygame"]

        self.debug = PYPYX.getboolean("debug")
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

    @classmethod
    def quit(self):
        import pygame
        pygame.quit()


Core.init()
sys.modules[__name__].__class__ = Core
