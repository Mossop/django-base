import os
import random
from configparser import ConfigParser

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def path(*x):
    return os.path.join(BASEDIR, *x)

BASE = os.path.basename(os.path.dirname(__file__))
PROJECT = os.path.basename(BASEDIR)

CONFIG = ConfigParser()
CONFIG.read(path("base", "defaults.ini"))

if "DATABASE_URL" in os.environ:
    CONFIG.set("general", "database", os.environ["DATABASE_URL"])
    CONFIG.set("general", "debug", "false")
else:
    CONFIG.set("general", "database", "sqlite3:///%s.sqlite" % PROJECT)

CONFIG.read(path("config", "config.ini"))
CONFIG.read(path("config.ini"))

if not CONFIG.has_option("security", "secret"):
    SECRET = ''.join([random.SystemRandom().choice(
        'abcdefghijklmnopqrstuvwxyz0123456789!@#$^&*(-_=+)') for i in range(50)])
    CONFIG.set("security", "secret", SECRET)

def merge_in(main, overrides):
    for (key, value) in overrides.items():
        if key in main:
            if isinstance(main[key], dict):
                main[key].update(value)
            else:
                main[key] = value
        else:
            main[key] = value
