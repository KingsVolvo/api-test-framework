import unittest
from api_test_model import ApiTestModel
from utils import *
from log_conf import Logger
import HTMLTestRunner
import requests


def add(a, b):
    return a + b


class ApiTestCase(unittest.TestCase):
    def set_apiurl_testmodel(self, url: str, testmodel: ApiTestModel):
        self.api_url = url
        self.api_test_model = testmodel

    def test_api_test_model(self):
        api_test_url = url_slicing(self.api_url, self.api_test_model.url)
        Logger.logr.info("url:{}".format(api_test_url))
        
        # 发送 HTTP 请求
        response = requests.request(
            self.api_test_model.method,
            api_test_url,
            params=self.api_test_model.params,
        )
        Logger.logr.info("response.code:{}, response.data:{}".format(response.status_code, response.json()))
        self.assertEqual(
            response.status_code, self.api_test_model.expected_response.get("code")
        )
        
        # 如果预期返回值中有data字段，判断返回值是否相等
        if self.api_test_model.expected_response.get("code") == 200:
            Logger.logr.debug("200 ok")
            if self.api_test_model.expected_response.get("body"):             
                self.assertEqual(
                    response.json(), self.api_test_model.expected_response.get("body")
                )
        


    def test_add(self):
        result = add(5, 3)
        self.assertEqual(result, 8)

    def runTest(self):
        self.test_api_test_model()
