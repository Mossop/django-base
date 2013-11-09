import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def path(*x):
    return os.path.join(BASEDIR, *x)

BASE = os.path.basename(os.path.dirname(__file__))
PROJECT = os.path.basename(BASEDIR)

def has_setting(name):
    try:
        import config
        if hasattr(config, name):
            return True
    except:
        pass
    return name in os.environ

def get_setting(name):
    try:
        import config
        if hasattr(config, name):
            return getattr(config, name)
    except:
        pass
    return os.environ[name]
