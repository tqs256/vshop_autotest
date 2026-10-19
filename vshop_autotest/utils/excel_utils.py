from pprint import pprint

import openpyxl
from jinja2 import Template
from config.config import *



class ExcelReader:

    def __init__(self,account_id=ACCOUNT_ID):

        self.file_path = FILE_PATH
        self.sheet_user_name = SHEET_USER_NAME
        self.sheet_case_name = SHEET_NAME
        self.account = account_id if account_id is not None else ACCOUNT_ID
        self.username = None
        self.password = None


    def _wb(self):

        wb = openpyxl.load_workbook(self.file_path)
        return wb

    def _load_user(self):

        wb = self._wb()
        ws = wb[self.sheet_user_name]
        for row in ws.iter_rows(min_row=self.account + 2,values_only=True):
            if row[0] == self.account:
                self.username = row[1]
                self.password = row[2]
                return
        raise ValueError (f"没有用户id为{self.account}的用户")

    def get_login_data(self):

        self._load_user()
        wb = self._wb()
        ws = wb[self.sheet_case_name]
        keys = [cell.value for cell in ws[2]]
        login_data = []
        for row in ws.iter_rows(min_row=3,max_row=3,values_only=True):
            dict_data = dict(zip(keys,row))
            template = Template(str(dict_data['json']))
            dict_data['json'] = template.render(
                username = self.username,
                password = self.password
            )
            login_data.append(dict_data)
        return login_data

    def get_business_data(self):

        wb = self._wb()
        ws = wb[self.sheet_case_name]
        start_row = 3
        for row in ws.iter_rows(min_row=3,values_only=True):
            if "/login" in str(row):
                start_row = 4
        keys = [cell.value for cell in ws[2]]
        business_data = []
        for row in ws.iter_rows(min_row=start_row,values_only=True):
            dict_data = dict(zip(keys,row))
            if "{{username}}" in str(dict_data) and "{{password}}" in str(dict_data):
                template = Template(str(dict_data['json']))
                dict_data['json'] = template.render(
                    username = self.username,
                    password = self.password
                )
            business_data.append(dict_data)
        return business_data




class Read_Excel:

    def __init__(self,account):
        """
        初始化

        Args:
            file_path: Excel 文件路径
            sheet_name: 工作表名称
        """
        self.file_path = FILE_PATH
        self.sheet_user_name = SHEET_USER_NAME
        self.sheet_case_name = SHEET_NAME
        self.account = account
        self.username = None
        self.password = None
        self._read_excel()

    def _get_user(self,workbook):
        worksheet = workbook[self.sheet_user_name]
        for row in worksheet.iter_rows(min_row=self.account,values_only=True):
            if row[0] == self.account:
                self.username = row[1]
                self.password = row[2]
                return
        raise  ValueError(f"没有id为{self.account}的账号")

    def _read_excel(self):

        workbook = openpyxl.load_workbook(self.file_path)
        self._get_user(workbook)
        worksheet = workbook[self.sheet_case_name]
        keys = [cell.value for cell in worksheet[2]]
        data = []
        for row in worksheet.iter_rows(min_row=3, max_row=worksheet.max_row,values_only=True):
            dict_data = dict(zip(keys,row))
            if dict_data['is_True']:
                template = Template(str(dict_data['json']))
                dict_data['json'] = template.render(
                    username = self.username,
                    password = self.password
                )
                data.append(dict_data)
        self.data = data



if __name__ == '__main__':
    A = ExcelReader()
    print(A.get_login_data())
    print(A.get_business_data())


