from django.test.runner import DiscoverRunner

from .config import TEST_MODE

class TestSuiteRunner(DiscoverRunner):
    def __init__(self, *args, **kwargs):
        if not TEST_MODE:
            raise Exception('Unexpected test run outside of test mode.')
        super(TestSuiteRunner, self).__init__(*args, **kwargs)
