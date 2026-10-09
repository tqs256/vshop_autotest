import logging

import requests


def send_http_request(**kwargs):
    resp = requests.request(**kwargs)
    logging.info(f"2,发送HTTP请求，响应：{resp.text}")
    return resp

# 数据库请求
