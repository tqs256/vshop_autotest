import logging

import requests

class request_util:
    def __init__(self):
        self.session = requests.session()
        self.logger = logging.getLogger(__name__)

    def send_http_request(self,**kwargs):
        resp = self.session.request(**kwargs)
        logging.info(f"2,发送HTTP请求，响应：{resp.text}")
        return resp

    # 数据库请求
