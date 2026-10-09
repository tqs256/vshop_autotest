import openpyxl
from jinja2 import Template
from config.config import *

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
    A = Read_Excel(1)
    print(A.data)

