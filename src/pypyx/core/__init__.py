# Importing
import logging
import os
import pypyx
import sys

from configparser import ConfigParser

logging.basicConfig(
    level=logging.DEBUG,
    filename=f"{os.path.dirname(__file__)}/logs.log",
    filemode="w",
    format="[%(name)s] %(levelname)s - %(message)s",
)


class Core(sys.modules[__name__].__class__):
    logger = logging.getLogger(__name__)

    config = ConfigParser()
    config.read([
        f"{os.getcwd()}/pypyx.ini",  # Custom configuration by user
        f"{os.path.dirname(__file__)}/pypyx.ini",  # Default configuration
    ])

    vsync_available = None

    @classmethod
    def init(self):
        # Managing configurations
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

        # LOGGING
        self.logger.info(f"Debug: {self.debug}")
        self.logger.info(f"Version: {pypyx.__version__}")
        self.logger.info(f"Pygame Support Prompt: {self.pygame_support_prompt}")

    @classmethod
    def quit(self):
        import pygame
        pygame.quit()


Core.init()
sys.modules[__name__].__class__ = Core
