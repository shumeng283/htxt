# Author :lixinhao
import requests
import json
import urllib3
from econtract_login import (login,ss)
import unittest
from Var import global_var

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class ht_qqjk(unittest.TestCase):
    '''确权列表'''
    def setUp(self):
        login()
    def test1_LPn(self):
        '''获取LP数量'''
        url = 'https://api.devraise.hffss.com/sign-trustee/prodTarget/findProdTargetList'
        headers = {
            "Host":" api.devraise.hffss.com",
            "Connection":" keep-alive",
            "Accept":" application/json, text/javascript, */*; q=0.01",
            "User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
            "Content-Type":" application/json",
            "Accept-Encoding":" gzip, deflate, br",
            "Accept-Language":" zh-CN,zh;q=0.9",
        }
        data = {
            "productName": "",
            "status": 99,
            "pageNumber": 1
        }
        r = ss.post(
            url=url,
            headers=headers,
            data=json.dumps(data)
        )
        print(r.json())

def suite():
    loginTestCase = unittest.makeSuite(ht_,"test")
    return loginTestCase

if __name__ == '__main__':
    unittest.main()