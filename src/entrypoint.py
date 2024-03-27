from core import *

from api_test_case import ApiTestCase
from HTMLTestRunner import HTMLTestRunner
from api_html_test_runner import CustomHTMLTestRunner
import unittest


if __name__ == "__main__":

    filename = "C:/Project/poc-everything/api-test/case.test"
    lines = filter_comments(filename=filename)
    Logger.logr.info(lines)
    (url, api_test_models) = parse_url_testmodel_url(lines)
    Logger.logr.debug("test_cases:{}".format(api_test_models))

    api_test_suite = ApiTestSuite()
   
    for model in api_test_models:
        api_test_case = ApiTestCase()
        api_test_case.set_apiurl_testmodel(url,model)
        api_test_suite.addTest(api_test_case)
 
    #unittest.TextTestRunner().run(api_test_suite)
    #runner = HTMLTestRunner(output='test-reports')
    runner = CustomHTMLTestRunner(output='test-reports')
    runner.run(api_test_suite)

    