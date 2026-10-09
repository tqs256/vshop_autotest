import logging


def http_assert(case,resp):
    if case['check'] == "message":
        result = resp.json().get('message')
        logging.info(f"3,HTTP响应断言内容： 预取结果: {case['expected']} == 实际结果: {result}")
        assert case['expected'] == result
    else:
        logging.info(f"3,HTTP响应断言内容： 预取结果:{case['expected']} in 实际结果:{resp.text}")
        assert case['expected'] in resp.text