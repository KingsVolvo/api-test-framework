import re
import json
from api_test_model import ApiTestModel
from pydantic import *


def filter_comments(filename):

    """
    过滤单行注释以#开头，多行#开头, 空格#开头
    Filter one line or multi-lines of comments
    """

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    # 匹配单行注释和多行注释
    pattern = re.compile(r"(\s+)?(#.*)|(\/\*.*?\*\/)|(\'\'\'.*?\'\'\')")
    filtered_lines = [line for line in lines if not pattern.match(line)]
    return "".join(filtered_lines)


# def url_slicing(prefix_url: str, api_test_model: ApiTestModel) -> str:
#     """if api_test_model.url doesn`t contains http or https, add url as prefix
#     Args:
#         prefix_url: prefix url
#     """
#     api_test_model_url = api_test_model.url

#     if not api_test_model_url.startswith(
#         "http://"
#     ) and not api_test_model_url.startswith("https://"):
#         api_test_model_url = f"{prefix_url}{api_test_model_url}"

#     return api_test_model_url


def parse_test_cases(data: list) -> list[ApiTestModel]:
    """Parses a list of dictionaries into ApiTestModel objects.

    Args:
        data (list): A list of dictionaries representing test cases.

    Returns:
        list[ApiTestModel]: A list of validated ApiTestModel objects.
    """

    parsed_cases = []
    for case in data:
        try:
            parsed_case = ApiTestModel(
                **case
            )  # Unpack dictionary into keyword arguments
            parsed_cases.append(parsed_case)
        except (ValidationError, ValueError) as e:
            print(f"Error parsing test case: {e}")

    return parsed_cases


def url_slicing(prefix_url: str, api_test_model_url: str) -> str:
    """if api_test_model_url doesn`t contains http or https, add url as prefix
    Args:
        prefix_url: prefix url
    """

    if not api_test_model_url.startswith(
        "http://"
    ) and not api_test_model_url.startswith("https://"):
        api_test_model_url = f"{prefix_url}{api_test_model_url}"

    return api_test_model_url
