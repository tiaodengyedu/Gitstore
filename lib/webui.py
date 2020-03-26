from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from hyrobot.common import *


def open_browser():
    # 打开浏览器
    driver = webdriver.Chrome()
    GSTORE['get_global_driver'] = driver
    return driver


def get_global_driver():
    return GSTORE['get_global_driver']


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


def check_login(driver):
    CHECK_POINT('检测是否登录', driver.title == '白月销售管理系统')


def add_medicines(driver, addlist):
    driver.find_element_by_css_selector('.fa.fa-plus').click()
    time.sleep(1)
    # 添加药品
    driver.find_element_by_css_selector('.add-one-area .btn-md').click()
    inputs = driver.find_elements_by_css_selector('.col-sm-8 .form-control')
    inputs[0].send_keys(addlist[0])
    inputs[1].send_keys(addlist[1])
    inputs[2].send_keys(addlist[2])
    driver.find_element_by_css_selector('.add-one-area .btn-xs').click()


def check_medicines(driver, addlist):
    driver.find_element_by_css_selector('.col-sm-12 .btn-xs').click()
    time.sleep(1)
    # 检查是否添加正确
    msgs = driver.find_elements_by_css_selector('.search-result-item span')
    msg = [i.text for i in msgs[0:6]]
    excepted = ['药品：',
                addlist[0],
                '编号：',
                addlist[1],
                '描述：',
                addlist[2]]
    CHECK_POINT('查看药品列表第一项', msg == excepted)


def add_customers(driver, addlist):
    driver.find_element_by_css_selector('.sidebar-menu .fa-user').click()
    time.sleep(1)
    driver.find_element_by_css_selector('div>[class="btn btn-green btn-outlined btn-md"]').click()
    inputs = driver.find_elements_by_class_name('form-control')
    inputs[0].send_keys(addlist[0])
    inputs[1].send_keys(addlist[1])
    inputs[2].send_keys(addlist[2])
    driver.find_element_by_css_selector('[class="btn btn-green btn-outlined btn-xs"]').click()


def check_customers(driver, addlist):
    results = driver.find_element_by_css_selector('div.search-result-item')
    msg = [result.text for result in results.find_elements_by_css_selector('span')[0:6]]

    expected = [
        '客户名：',
        addlist[0],
        '联系电话：',
        addlist[1],
        '地址：',
        addlist[2]]

    # 检查添加信息是否正确
    CHECK_POINT('检查客户信息是否正确', msg == expected)


def add_orders(driver, addorders):
    driver.find_element_by_css_selector('.fa.fa-paperclip').click()
    time.sleep(1)
    driver.find_element_by_css_selector('.add-one-area .btn-md').click()
    time.sleep(1)

    driver.find_element_by_css_selector('.col-sm-8 .form-control').send_keys(addorders[0])

    xxxs = driver.find_elements_by_css_selector('.col-sm-8 .xxx')
    select = Select(xxxs[0])
    select.select_by_visible_text(addorders[1])
    time.sleep(1)
    addorders1 = addorders[2][0::2]
    addorders2 = addorders[2][1::2]
    # INFO(addorders1)
    # INFO(addorders2)

    n = 0
    for i in addorders1:
        select = Select(xxxs[1])
        select.select_by_visible_text(i)
        time.sleep(1)
    madis = driver.find_elements_by_css_selector('.col-sm-12 [style="margin-top: 0.2em;"]')
    for i in addorders2:
        input1 = madis[n].find_element_by_css_selector('input')
        input1.send_keys(i)
        n += 1
    driver.find_element_by_css_selector('.col-sm-12 .btn-xs').click()


def check_orders(driver, addorders):
    msg = []
    results1 = driver.find_elements_by_css_selector('.search-result-item .search-result-item-field span')
    for i in results1[0:7]:
        if i.text != results1[2].text and i.text != results1[3].text:
            msg.append(i.text)
    results2 = driver.find_element_by_css_selector('.search-result-item .search-result-item-field p').text
    msg.append(results2)
    # INFO(msg)
    CHECK_POINT('订单信息检查', msg == addorders)