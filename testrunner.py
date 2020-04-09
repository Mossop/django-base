from django.conf import settings
from django.test.runner import DiscoverRunner

from .utils import CONFIG, path

class TestSuiteRunner(DiscoverRunner):
    def __init__(self, *args, **kwargs):
        settings.TEST_MODE = True
        CONFIG.read(path('test.ini'))
        super(TestSuiteRunner, self).__init__(*args, **kwargs)
