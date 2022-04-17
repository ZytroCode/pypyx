# Importing
import os
import sys

from configparser import ConfigParser


# Config class
class Config(sys.modules[__name__].__class__):
    # Getting the configuration file
    file = ConfigParser()

    path = f"{os.getcwd()}\\pypyx.ini"
    default_path = f"{os.path.dirname(__file__)}\\pypyx.ini"

    file.read([default_path, path])


sys.modules[__name__].__class__ = Config
