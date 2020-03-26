from common.common2 import *
from selenium import webdriver
import time

def open_browser():
    driver = webdriver.Chrome()
    GSTORE["get_global_driver"] = driver
    return driver


def get_global_driver():
    return GSTORE["get_global_driver"]


def admin_login(driver):
    driver.get('http://127.0.0.1/mgr/sign.html')
    driver.implicitly_wait(5)
    # 管理员登录
    ele = driver.find_element_by_css_selector('.form-group.has-feedback')
    user = ele.find_element_by_tag_name('input')
    passwd = driver.find_element_by_id('password')
    user.send_keys('byhy')
    passwd.send_keys('88888888')
    driver.find_element_by_css_selector('[class="btn btn-primary btn-block btn-flat"]').click()

    time.sleep(2)


