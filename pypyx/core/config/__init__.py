# Importing
import os
import sys

from configparser import ConfigParser


# Config class
class Config(sys.modules[__name__].__class__):
    # Getting the configuration file
    file = ConfigParser()
    configs = [
        f"{os.getcwd()}\\pypyx.ini",
        f"{os.path.dirname(__file__)}\\pypyx.ini"
    ]

    file.read(configs)


sys.modules[__name__].__class__ = Config
