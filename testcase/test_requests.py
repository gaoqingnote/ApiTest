import requests
import logging
import pytest
import json


class TestRequest(object):
    logging.basicConfig(level=logging.INFO)
    #logging.getLogger().setLevel(logging.INFO)

    url = 'http://testerhome.com/api/v3/topics.json?limit=2'

    def test_get(self):
        r=requests.get(self.url)
        #r.contest 是字节类型
        print(type(r.content))
        print(r.status_code)
        print(r.url)
        print(r.content)
        print(str(r.content))
        #r.json是使用了json.loads()方法返回的字典类型数据
        print(type(r.json()))
        #json的类型是字符串，字典的类型是字典
        remp = json.dumps(r.json(), indent=2) #将字典序列化为字符串
        print(type(remp))
        print(remp)
        print(r.headers)
        print(r.text)
        print(logging.info(r))


    #def test_post(self):
        #r=requests.post(self.url,data=payload)
       # print(json.dumps(r.json(),indent=2))
