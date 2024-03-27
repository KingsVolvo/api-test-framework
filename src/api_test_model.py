from pydantic import BaseModel, HttpUrl, conlist, validator, ValidationError
from log_conf import Logger
import requests


class ApiTestModel(BaseModel):
    method: str
    url: str
    params: str
    expected_response: dict

    # 验证method必须是GET或POST
    @validator("method")
    def validate_method(cls, v):
        if v not in ["GET", "POST"]:
            raise ValueError("method must be GET or POST")
        return v

    # 验证expected_response的结构
    @validator("expected_response")
    def validate_expected_response(cls, v):
        if not isinstance(v, dict) or "code" not in v or "body" not in v:
            raise ValueError("expected_response must contain code and body")
        return v


# def run(self, api_url_prefix):
#     try:
#         self.call_func(api_url_prefix)
# # 检查响应是否正确
# if response.status_code != api_test["expected_response"]["code"]:
#     print(f"测试用例失败：{api_test['method']} {api_test['url']}")
#     print(f"预期响应代码：{api_test['expected_response']['code']}")
#     print(f"实际响应代码：{response.status_code}")
#     exit(1)

# if json.loads(response.content) != api_test["expected_response"]["body"]:
#     print(f"测试用例失败：{api_test['method']} {api_test['url']}")
#     print(f"预期响应体：{api_test['expected_response']['body']}")
#     print(f"实际响应体：{json.loads(response.content)}")
#     exit(1)
#         Logger.logr.info("url:{},method:{},params:{}, result:Passed".format(self.url,self.method,self.params))
#     except AssertionError as e:
#         Logger.logr.error("url:{},method:{},params:{}, result:Failed".format(self.url,self.method,self.params))
#     except NameError as e:
#         Logger.logr.error("url:{} Failed -- Function: Call_func not defined.error:{}".format(self.url, e))


# if __name__ == "__main__":
#     TEST_CASES = [
#         {
#             "method": "GET",
#             "url": "/users",
#             "params": "",
#             "expected_response": {
#                 "code": 200,
#                 "body": {
#                     "users": [
#                         {"id": 1, "name": "John Doe"},
#                         {"id": 2, "name": "Jane Doe"},
#                     ]
#                 },
#             },
#         },
#         {
#             "method": "POST",
#             "url": "/users",
#             "params": "name=John Doe&email=johndoe@example.com",
#             "expected_response": {
#                 "code": 201,
#                 "body": {"id": 3, "name": "John Doe", "email": "johndoe@example.com"},
#             },
#         },
#     ]

#     parsed_cases = parse_test_cases(TEST_CASES)
#     for case in parsed_cases:
#         print(case)
