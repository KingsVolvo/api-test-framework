from core import *

from api_test_case import ApiTestCase
from HTMLTestRunner import HTMLTestRunner
from api_html_test_runner import CustomHTMLTestRunner
import unittest
import os
import glob

dir = "/app/api-test/"

if __name__ == "__main__":

    # unittest.TextTestRunner().run(api_test_suite)
    runner = HTMLTestRunner(output="test-reports")

    for file_path in glob.glob(os.path.join(dir, "*.test")):
        filename = os.path.splitext(os.path.basename(file_path))[0]
        lines = filter_comments(file_path=file_path)
        Logger.logr.info(lines)
        (url, api_test_models) = parse_url_testmodel_url(lines)
        Logger.logr.debug("test_cases:{}".format(api_test_models))

        api_test_suite = ApiTestSuite()

        for model in api_test_models:
            api_test_case = ApiTestCase()
            api_test_case.set_apiurl_testmodel(url, model)
            api_test_suite.addTest(api_test_case)

        # runner = CustomHTMLTestRunner(output='test-reports')
        runner.run(api_test_suite)
