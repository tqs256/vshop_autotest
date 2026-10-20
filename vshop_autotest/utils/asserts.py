import logging



class Assertions:

    @staticmethod
    def assert_status_code(resp,expected:int = 200):
        actual = resp.status_code
        assert actual == expected,(
            f"http状态码不匹配\n"
            f"实际:{actual}\n"
            f"预取:{expected}\n"
            f"响应体：{resp.text}\n"
        )
        logging.info(f"http断言成功，预取结果：{expected} == 实际结果:{actual}")


def http_assert(case,resp):
    if case['check'] == "message":
        result = resp.json().get('message')
        logging.info(f"3,HTTP响应断言内容： 预取结果: {case['expected']} == 实际结果: {result}")
        assert case['expected'] == result
    else:
        logging.info(f"3,HTTP响应断言内容： 预取结果:{case['expected']} in 实际结果:{resp.text}")
        assert case['expected'] in resp.text


