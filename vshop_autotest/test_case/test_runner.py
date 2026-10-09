import logging
from jinja2 import Template
import pytest
import requests
import jsonpath
from vshop_autotest.utils.analyse_case import AnalyseCase
from vshop_autotest.utils.asserts import http_assert
from vshop_autotest.utils.excel_utils import Read_Excel
from vshop_autotest.utils.extractor import json_extractor
from vshop_autotest.utils.send_request import send_http_request


class Testrunner:

    # 读取测试文件中的数据，用属性保存
    data = Read_Excel(1).data
    # 5：提取后的数据需要初始化一个全局的属性来保存
    all = {}

    @pytest.mark.parametrize('case',data)
    def test_case(self,case):

        all = self.all
        case = eval(Template(str(case)).render(all))

        # 0：测试用例的描述信息
        logging.info(f"用例id：{case["id"]}，模块：{case["feature"]}")

        # 1：解析请求数据
        print(case)
        analyse_data= AnalyseCase(case)
        request_data = analyse_data.analyse_case()

        # 2：发起请求
        resp = send_http_request(**request_data)
        # print(resp.json())

        # 3：处理断言
        http_assert(case,resp)

        # 4：提取所需数据（提取到外层）
        json_extractor(case,all,resp)

        # try:
        #     token = eval(case['jsonExData']) if isinstance(case['jsonExData'],str) else None
        #     print(type(token))
        #     for key,value in token.items():
        #         pass
        # except Exception as e:
        #     print("没有提取到jsonExData",e)
