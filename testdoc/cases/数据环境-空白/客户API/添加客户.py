from lib.webapi import adminapi
from common.common import *

force_tags = ['冒烟']


class C1:

    name = 'API-0151'

    def __init__(self):
        self.addedCustomerId = None

    def teardown(self):
        adminapi.customer_del(self.addedCustomerId)

    def teststeps(self):

        STEP(1, '添加一个客户')
        res = adminapi.customer_add('武汉市桥西医院',
                                    '13345679934',
                                    '武汉市桥西医院北路')
        addret = res.json()
        CHECK_POINT('返回的ret值为0', addret['ret'] == 0)
        self.addedCustomerId = addret['id']

        STEP(2, '检查添加的客户信息')
        res = adminapi.customer_list(100, 1, '')
        listret = res.json()
        expected = {"ret": 0,
                    "retlist": [
                                {"address": "武汉市桥西医院北路",
                                 "id": addret['id'],
                                 "name": "武汉市桥西医院",
                                 "phonenumber": "13345679934"
                                 }],
                    'total': 1}
        CHECK_POINT('检查是否添加正确', listret == expected)


class C2:
    name = 'API-0152'

    def __init__(self):
        self.setupcustomercid = None
        self.addedCustomerId = None

    def setup(self):

        INFO('增加10个客户')
        self.setupcustomercid = []
        for i in range(10):
            res = adminapi.customer_add(f'武汉市桥西医院_{i+1}',
                                        f'1000000000{i}',
                                        f'武汉市桥西医院北路_{i+1}')
            self.setupcustomercid.append(res.json()['id'])

    def teardown(self):

        adminapi.customer_del(self.addedCustomerId)
        for cid in self.setupcustomercid:
            adminapi.customer_del(cid)

    def teststeps(self):

        STEP(1, '先列出客户')
        res = adminapi.customer_list(10, 1, '')
        listret = res.json()
        customerlistBefore = listret['retlist']

        STEP(2, '添加一个客户')
        res = adminapi.customer_add('南京市桥西医院',
                                    '13345679934',
                                    '南京市桥西医院北路')
        addret = res.json()
        CHECK_POINT('返回的ret值为0', addret['ret'] == 0)
        self.addedCustomerId = addret['id']

        STEP(3, '检查添加的客户信息')
        res = adminapi.customer_list(11, 1, '')
        listret = res.json()
        expected = {"ret": 0,
                    "retlist": [
                                {"address": "南京市桥西医院北路",
                                 "id": addret['id'],
                                 "name": "南京市桥西医院",
                                 "phonenumber": "13345679934"
                                 }] + customerlistBefore,
                    'total': 11}
        CHECK_POINT('检查是否添加正确', listret == expected)


class C3:

    name = 'API-0153'
    tags = ['触发错误']

    @staticmethod
    def teststeps():
        STEP(1, '添加一个客户')
        data = {"phonenumber": "13345679934",
                "address": "武汉市桥西医院北路"}
        res = adminapi.customer_add2(data)
        addret = res.json()
        CHECK_POINT('返回值', addret == {"ret": 1,
                                      "msg":  "请求消息参数错误"})

        STEP(2, '检查客户信息')
        res = adminapi.customer_list(100, 1, '')
        listret = res.json()
        expected = {"ret": 0,
                    "retlist": [],
                    'total': 0}
        CHECK_POINT('检查是否添加正确', listret == expected)
