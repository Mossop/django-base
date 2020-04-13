import logging

from django.test.runner import DiscoverRunner

from .config import TEST_MODE

class TestSuiteRunner(DiscoverRunner):
    def __init__(self, *args, **kwargs):
        if not TEST_MODE:
            raise Exception('Unexpected test run outside of test mode.')

        logger = logging.getLogger('django')
        logger.setLevel(logging.ERROR)
        super(TestSuiteRunner, self).__init__(*args, **kwargs)
