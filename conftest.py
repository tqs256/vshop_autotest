import jsonpath
import pytest
from vshop_autotest.utils.analyse_case import AnalyseCase
from vshop_autotest.utils.excel_utils import ExcelReader
from vshop_autotest.utils.send_request_util import request_util


@pytest.fixture(scope="session")
def get_token():

    # 从excel读取登录接口
    read_excel = ExcelReader()
    login_data = read_excel.get_login_data()

    # 解析登录接口数据
    Analysecase = AnalyseCase(login_data)
    login_case = Analysecase.analyse_case()

    # 发送请求
    send_request = request_util()
    resp = send_request.send_http_request(**login_case)

    # 获取token值
    token = jsonpath.jsonpath(resp.json(),"$..token")[0]
    return token


@pytest.fixture(scope="session")
def build_token(get_token):
    return {"Authorization": f"Bearer {get_token}"}


@pytest.fixture(scope="session")
def auth_token(build_token):
    request = request_util()
    request.session.headers.update(build_token)
    yield request
    request.session.close()


