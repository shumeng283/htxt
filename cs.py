# Author :lixinhao
from locust import HttpLocust,TaskSet,task
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class login(TaskSet):
    '''登录'''
    @task(1)
    def login_test1(self):
        #定义request请求头
        header = {
            "Accept":" application/json, text/javascript, */*; q=0.01",
            "User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
            "Content-Type":" application/json",
            "Accept-Encoding":" gzip, deflate, br",
            "Accept-Language":" zh-CN,zh;q=0.9",
        }
        #请求主体
        data = {
            "userName":"527522643@qq.com",
            "password":"s123456"
        }
        #发送请求
        r = self.client.post(
            '/sign-trustee/user/login',
            header=header,
            data=data,
            verify=False
        )
        print(r.status_code)
        assert r.status_code == 200

class websiteUser(HttpLocust):
    task_set = BlogDemo
    min_wait = 3000  # 单位毫秒
    max_wait = 6000  # 单位毫秒

if __name__ == "__main__":
    import os
    os.system("locust -f demo.py --host=https://api.raise.hffss.com")