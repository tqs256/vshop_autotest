import logging
from pprint import pprint
from unittest import case

from config.config import BASE_URL
from vshop_autotest.utils.excel_utils import Read_Excel, ExcelReader


class AnalyseCase():
    def __init__(self,case):

        self.case = case[0] if isinstance(case, list) else case


    def analyse_case(self):

        method = self.case['method']
        url = BASE_URL + self.case['path']
        headers = eval(self.case['headers']) if isinstance(self.case['headers'], str) else None
        params = eval(self.case['params']) if isinstance(self.case['params'], str) else None
        data = eval(self.case['data']) if isinstance(self.case['data'], str) else None
        json = eval(self.case['json']) if isinstance(self.case['json'], str) else None

        request_data = {
            'method': method,
            'url': url,
            'headers': headers,
            'params': params,
            'json': json,
            'data': data
        }
        logging.info(f"1,解析请求数据，请求数据为{request_data}")
        return request_data

if __name__ == '__main__':
    R = ExcelReader()
    r = R.get_business_data()
    A = AnalyseCase(r)
    print(A.analyse_case())