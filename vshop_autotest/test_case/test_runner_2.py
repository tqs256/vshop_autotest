import logging
from pprint import pprint

import jsonpath
import pytest
from jinja2 import Template

from vshop_autotest.utils.analyse_case import analyse_case
from vshop_autotest.utils.asserts import http_assert
from vshop_autotest.utils.excel_utils import read_excel
from vshop_autotest.utils.extractor import json_extractor
from vshop_autotest.utils.send_request import send_http_request


class Test_runner_2:

    # 全局字典保存token
    all_data = {}

    # 1，读取excel中的数据
    data = read_excel(sheet_name='Sheet2')
    # pprint(data)

    @pytest.mark.parametrize('case',data)
    def test_case(self,case):

        rendered = Template(str(case)).render(self.all_data)
        case = eval(rendered)
        # pprint(case)
        # 2，解析请求数据
        logging.info(f"用例id；{case['case_id']},用例场景：{case["story"]}")
        request_data = analyse_case(case)
        # pprint(request_data)
        # 3，发送请求
        resp = send_http_request(**request_data)
        # pprint(resp)

        # 4，解析断言
        http_assert(case,resp)
        # 5，提取token
        # json_extractor(case,self.all_data,resp)
        json_extractor(case,self.all_data,resp)