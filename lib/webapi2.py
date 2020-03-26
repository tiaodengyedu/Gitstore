import requests
from hyrobot.common import *


class AdminApi:
    """
    接口
    """
    def __init__(self):
        self.s = requests.Session()

    @staticmethod
    def __printResponse(response):
        INFO('\n\n----HTTP response * begin ----')
        INFO(response.status_code)
        for k, v in response.headers.items():
            INFO(f'{k},{v}')
        INFO('')
        INFO(response.content.decode('utf8'))
        INFO('----HTTP response * end ----\n\n')

    def adminLogin(self, username, password, useProxy=False):
        if useProxy:
            self.s.proxies.update({'http': '127.0.0.1:8888', 'https': '127.0.0.1:8888'})
        response = self.s.post('http://127.0.0.1/api/mgr/signin',
                               data={'username': username,
                                     'password': password})
        self.__printResponse(response)
        return response
