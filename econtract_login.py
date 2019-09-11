# -*- coding: utf-8 -*-
import requests
import json

ss = requests.Session()

def login():
    """
    登陆
    :return:
    """
    username = "wagnere@163.com"
    password = "s123456"

    default_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "Content-Type": "application/json",
    }
    login_url = "https://api.devraise.hffss.com/sign-manager/user/login"
    data = {
        "userName": username,
        "password": password
    }
    ss.head(
        login_url,
        data=json.dumps(data),
        headers=default_headers,
    )
    res = ss.post(
        login_url,
        data=json.dumps(data),
        headers=default_headers,
    )
    print(res.json())


if __name__ == '__main__':
    login()