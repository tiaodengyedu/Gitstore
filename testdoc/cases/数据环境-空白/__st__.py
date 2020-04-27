from lib.webapi import adminapi
from common.common import *


def suite_setup():
    INFO('删除所有客户，药品，订单信息')
    adminapi.admin_login('byhy', '88888888')
    adminapi.order_del_all()
    adminapi.customer_del_all()
    adminapi.medicine_del_all()
