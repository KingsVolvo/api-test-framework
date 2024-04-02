from utils import *
from api_test_model import *
from api_test_suite import ApiTestSuite
from pydantic import *
from typing import Tuple
from log_conf import Logger
import requests


def parse_url_testmodel_url(lines) -> Tuple[str, list[ApiTestModel]]:
    """
    Parse from test case file into ( Api_url, list[ApiTestModel] )
    """

    pattern = re.compile(r"API_URL\s*=\s*\"(.*?)\"")
    match = pattern.match(lines)

    if match:
        api_url = match.group(1)
        Logger.logr.info(f"API URL: {api_url}")
    else:
        Logger.logr.info("API URL not found")

    sub_lines = pattern.sub("", lines)
    print(f"sub_lines:{sub_lines}")

    api_test_model_object = eval(sub_lines[sub_lines.find("=") + 1 :])

    # 将api_test_model解析为api_test_model对象列表
    api_tests = parse_test_cases(api_test_model_object)

    Logger.logr.info(f"Test case: {api_tests}")

    return (api_url, api_tests)


if __name__ == "__main__":
    filename = "C:/Project/poc-everything/api-test/case.test"
    lines = filter_comments(filename=filename)
    Logger.logr.info(lines)
    (url, test_cases) = parse_url_testmodel_url(lines)
    Logger.logr.debug("test_cases:{}".format(test_cases))

    api_test_suite = ApiTestSuite(test_cases)
