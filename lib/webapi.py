import requests

from hyrobot.common import *


class AdminApi:
    """
    接口
    """
    def __init__(self):
        self.s = requests.Session()

    @staticmethod
    def _printResponse(response):
        INFO('\n\n-------- HTTP response * begin -------')
        INFO(response.status_code)
        for k, v in response.headers.items():
            INFO(f'{k}:{v}')
        INFO('')
        INFO(response.content.decode('utf-8'))
        INFO('-------- HTTP response * end -------\n\n')

    def admin_login(self, username, password, useProxy=False):
        if useProxy:
            self.s.proxies.update({'http': '127.0.0.1:8888'})

        response = self.s.post('http://127.0.0.1/api/mgr/signin',
                               data={'username': username,
                                     'password': password})

        self._printResponse(response)
        return response

    def customer_list(self, pagesize=10, pagenumber=1, keywords=''):
        INFO('列出客户')
        response = self.s.get('http://127.0.0.1/api/mgr/customers',
                              params={
                                  'action': 'list_customer',
                                  'pagesize': pagesize,
                                  'pagenum': pagenumber,
                                  'keywords': keywords
                              })
        self._printResponse(response)
        return response

    def medicine_list(self, pagesize=10, pagenumber=1, keywords=''):
        INFO('列出药品')
        response = self.s.get('http://127.0.0.1/api/mgr/medicines',
                              params={
                                  'action': 'list_medicine',
                                  'pagesize': pagesize,
                                  'pagenum': pagenumber,
                                  'keywords': keywords
                              })
        self._printResponse(response)
        return response

    def order_list(self, pagesize=10, pagenumber=1, keywords=''):
        INFO('列出订单')
        response = self.s.get('http://127.0.0.1/api/mgr/orders',
                              params={
                                  'action': 'list_order',
                                  'pagesize': pagesize,
                                  'pagenum': pagenumber,
                                  'keywords': keywords
                              })
        self._printResponse(response)
        return response

    def customer_add(self, name, phonenumber, address):
        INFO('添加客户')
        response = self.s.post('http://127.0.0.1/api/mgr/customers',
                               json={"action": "add_customer",
                                     "data": {
                                              "name": name,
                                              "phonenumber": phonenumber,
                                              "address": address
                                             }})
        self._printResponse(response)
        return response

    def customer_add2(self, data):
        INFO('添加客户')
        response = self.s.post('http://127.0.0.1/api/mgr/customers',
                               json={"action": "add_customer",
                                     "data": data})
        self._printResponse(response)
        return response

    def customer_del(self, cid):
        INFO('删除客户')
        response = self.s.delete('http://127.0.0.1/api/mgr/customers',
                                 json={"action": "del_customer",
                                       "id": cid})
        self._printResponse(response)
        return response

    def customer_del_all(self):
        INFO('删除全部客户')
        response = self.customer_list(100, 1, '')
        thelist = response.json()['retlist']
        for customer in thelist:
            self.customer_del(customer['id'])

    def medicine_del(self, mid):
        INFO('删除药品')
        response = self.s.delete('http://127.0.0.1/api/mgr/medicines',
                                 json={"action": "del_medicine",
                                       "id": mid}
                                 )
        self._printResponse(response)
        return response

    def medicine_del_all(self):
        INFO('删除全部药品')
        response = self.medicine_list(100, 1, '')
        thelist = response.json()['retlist']
        for medicine in thelist:
            self.medicine_del(medicine['id'])

    def order_del(self, oid):
        INFO('删除订单')
        response = self.s.delete('http://127.0.0.1/api/mgr/orders',
                                 json={"action": "delete_order",
                                       "id": oid}
                                 )
        self._printResponse(response)
        return response

    def order_del_all(self):
        INFO('删除全部订单')
        response = self.order_list(100, 1, '')
        thelist = response.json()['retlist']
        for order in thelist:
            self.order_del(order['id'])


adminapi = AdminApi()
