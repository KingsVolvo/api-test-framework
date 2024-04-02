from api_test_model import ApiTestModel
from api_test_case import ApiTestCase
from log_conf import Logger
import unittest


class ApiTestSuite(unittest.TestSuite):
    def addTest(self, testcase: unittest.TestCase):
        super().addTest(testcase)

    def run(self, result: unittest.TestResult):
        Logger.logr.info("start to run api test suite.")
        super().run(result)
