# Author :lixinhao
import requests
import json
import urllib3
from econtract_login import (login,ss)
import unittest
from Var import global_var

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class ht_details(unittest.TestCase):
    '''合同详情页'''
    def setUp(self):
        login()
    def test1_people(self):
        '''添加投资人'''
        url = 'https://api.devraise.hffss.com/sign-manager/template/createContractByImportInvestor'
        headers = {
            "Connection":"keep-alive",
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0",
            "Content-Type":"application/json",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"zh-CN,zh;q=0.8"
        }
        data = {"templateId":456,"investList":[{"authId":422,"investType":2}]}
        r = ss.post(
            url=url,
            headers=headers,
            data=json.dumps(data)
        )
        self.assertEqual(r.json()['status'],'success')
    def test2_findId(self):
        '''确定未发起合同'''
        url = 'https://api.devraise.hffss.com/sign-manager/template/findContractConfigureByTemplateId'
        headers = {
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding":"gzip, deflate, sdch, br",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Connection":"keep-alive",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0",
        }
        par = {
            "templateId" : 456,
            "_" : 1566803068383
        }
        r = ss.get(
            url=url,
            headers=headers,
            params=par
        )
        listid = list(r.json()['data']['configureList'])
        for i in listid:
            if i['sendInvestorFlag'] is None:
                global_var['var'] = i['contractId']
                print(global_var['var'])
                return
    def test3_sendHT(self):
        '''发送合同To投资人'''
        url = 'https://api.devraise.hffss.com/sign-manager/template/sendToInvestors'
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0",
        }
        data = {
            'signContractIds' : [global_var['var']],
            'messageFlag': 0,
            'emailFlag': 0,
            'wechatFlag': 1
        }
        ss.options(
            url=url,
            headers=headers,
            data=json.dumps(data)
        )
        r = ss.post(
            url=url,
            headers=headers,
            data=json.dumps(data)
        )
        print(r.json())
        self.assertEqual(r.json()['status'],'success')

def suite():
    loginTestCase = unittest.makeSuite(ht_,"test")
    return loginTestCase

if __name__ == '__main__':
    unittest.main()