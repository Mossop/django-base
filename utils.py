import os
import random
from ConfigParser import ConfigParser

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def path(*x):
    return os.path.join(BASEDIR, *x)

BASE = os.path.basename(os.path.dirname(__file__))
PROJECT = os.path.basename(BASEDIR)

config = ConfigParser()
config.read(path("base", "defaults.ini"))

if "VCAP_APPLICATION" in os.environ:
    # Hosts/domain names that are valid for this site; required if DEBUG is False
    # See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
    vcap_app = json.loads(os.environ["VCAP_APPLICATION"])
    config.set("security", "hosts", vcap_app['uris'])
    config.set("general", "debug", "false")

if "DATABASE_URL" in os.environ:
    config.set("general", "database", os.environ["DATABASE_URL"])
    config.set("general", "debug", "false")
else:
    config.set("general", "database", "sqlite3:///%s" % path("%s.sqlite" % PROJECT))

config.read(path("config.ini"))

if not config.has_option("security", "secret"):
    secret = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
    config.set("security", "secret", secret)
