from common.common import *
from lib.LoginPage import LoginPage
from lib.Browser import Browser
from lib.HomePage import HomePage


def suite_setup():
    # 创建 浏览器
    browser = Browser()
    browser.open_browser()
    browser.openUrl()


def suite_teardown():
    driver = GSTORE['getGlobalDriver']
    driver.quit()


class C1:
    name = 'UI-0101'

    def teststeps(self):

        driver = GSTORE['getGlobalDriver']
        # 登录
        loginPage = LoginPage(driver)

        loginPage.login('byhy', '88888888')
        # 登录检查
        loginPage.sleep(1)
        homePage = HomePage(driver)
        homePage.checkLogin()
        # 获取侧边栏文本
        SI = homePage.getText(homePage.siderinner)
        # 检查文本是否正确
        CHECK_POINT('侧边栏文本检查', SI[0:3] == ['客户', '药品', '订单'])

