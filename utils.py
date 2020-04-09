import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def path(*x):
    return os.path.join(BASEDIR, *x)

def merge_in(main, overrides):
    for (key, value) in overrides.items():
        if key in main:
            if isinstance(main[key], dict):
                main[key].update(value)
            else:
                main[key] = value
        else:
            main[key] = value

class PathConfig:
    def __init__(self, config):
        self.config = config

    def get(self, name):
        if self.config.has_option('path', name):
            return path(self.config.get('path', name))

        return path(name)
