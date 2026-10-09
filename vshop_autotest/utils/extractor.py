import jsonpath
import logging


def json_extractor(case,all_data: dict,resp):
    if case['jsonExData']:
        for item in eval(case['jsonExData']):
            print(item,type(item))
            for key, value in dict(item).items():
                if key == "TOKEN":
                    v = 'Bearer ' + jsonpath.jsonpath(resp.json(), value)[0]
                    all_data[key] = v
                else:
                    v = jsonpath.jsonpath(resp.json(), value)[0]
                    all_data[key] = v
                print(all_data)
        logging.info(f"4,JSON提取，根据{case['jsonExData']}提取数据，此时全局变量为{all_data}")
