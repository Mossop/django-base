import os
import sys
import random
from configparser import ConfigParser

from .utils import BASEDIR, path, PathConfig

BASE = os.path.basename(os.path.dirname(__file__))
PROJECT = os.path.basename(BASEDIR)

CONFIG = ConfigParser()
CONFIG.read(path("base", "defaults.ini"))

if "DATABASE_URL" in os.environ:
    CONFIG.set("general", "database", os.environ["DATABASE_URL"])
else:
    CONFIG.set("general", "database", "sqlite3:///%s.sqlite" % PROJECT)

CONFIG.read(path("config", "config.ini"))
CONFIG.read(path("config.ini"))

TEST_MODE = False

if "TEST_MODE" in os.environ:
    TEST_MODE = True
else:
    for i in range(len(sys.argv) - 1):
        if sys.argv[i][-9:] == "manage.py":
            if sys.argv[i + 1] == "test":
                TEST_MODE = True
            break

if TEST_MODE:
    CONFIG.read(path("test.ini"))

if not CONFIG.has_option("security", "secret"):
    SECRET = ''.join([random.SystemRandom().choice(
        'abcdefghijklmnopqrstuvwxyz0123456789!@#$^&*(-_=+)') for i in range(50)])
    CONFIG.set("security", "secret", SECRET)

PATHS = PathConfig(CONFIG)
