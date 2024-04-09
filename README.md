# api-test-framework
Api test framework for test-api

# BA— Why need api test?

---

Api(Restful api) is always the interface between backend and frontend.

**Main Reasons for API Testing:**

1. **Ensure Functionality and Reliability:**
    - Verifies that the API meets its functional requirements and performs as intended.
    - Identifies and addresses bugs, errors, or inconsistencies that could affect the API's reliability and availability.
2. **Validate Data Integrity:**
    - Checks the accuracy, consistency, and completeness of data exchanged through the API.
    - Ensures that data is not corrupted or manipulated during transmission and processing.
3. **Test Performance and Scalability:**
    - Evaluates the API's performance under various load conditions and scenarios.
    - Identifies bottlenecks and optimizes the API to handle increased usage and maintain acceptable response times and throughput.

When in development,  at the minimum cost to identify Design vs. Implementation Differences automatically.  

# Solution.

---

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ef27a52-ac58-4320-949c-497eac996a73/413818c2-ea09-410f-88cc-d97e1656a158/Untitled.png)

### *.test file format

```bash
#定义API接口 URL
API_URL = "http://47.115.214.0:5555"

#定义测试用例
TEST_CASES = [
    {
        "method": "GET",
        "url": "/hello",
        "params": "",
        "expected_response": {
            "code": 200,
            "body": {
              "Hello":"ERROR"
            }
        }
    }
]

```

### Dockerfile

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ef27a52-ac58-4320-949c-497eac996a73/e86aa478-ea80-4de3-be13-a337c4e3edbf/Untitled.png)

### Main Points:

- Each test file only has 1 API_URL（Fixed name） and multipul TEST_CASES. (TEST_CASES can rename).
- **Method**: support GET, POST now.
- Check code and body consistency.
- Should easy to test, can be test in any folder with the same file structure.
- Dockfile is necessary.

### 

# CICD

---

github:

```bash
https://github.com/KingsVolvo/api-test-framework.git

```

PS: “**[dosubot](https://github.com/apps/dosubot) bot** ” can be used in personal project

image registry address

```bash
Aliyun:  
registry.cn-hangzhou.aliyuncs.com/kinghuang/api-test-framework:1158

AWS:
477069922492.dkr.ecr.cn-northwest-1.amazonaws.com.cn/api-test-framework

JFrog:
（waiting for permission）
```

# Test

---

1. docker build -t api-test-img .



1. docker run api-test-img


1. sh get_testapi_result.sh

