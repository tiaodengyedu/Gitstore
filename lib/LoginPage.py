from lib.BasePage import BasePage
from common.common import *


class LoginPage(BasePage):
    """
    登录页面
    """

    def __init__(self, driver):
        super().__init__(driver)
        # 定位登录框
        self.loginBox = self.find_element('css', '.form-group.has-feedback')
        # 定位用户框
        self.userEle = self.find_element('t', 'input', self.loginBox)
        # 定位密码框
        self.passWd = self.find_element('id', 'password')
        # 定位提交
        self.submitEle = self.find_element('css', '[class="btn btn-primary btn-block btn-flat"]')

    def login(self, user, pd):
        """
        登录
        :param user: 用户名
        :param pd: 密码        :
        """

        # 输入用户名 密码
        self.type(self.userEle, user)
        self.type(self.passWd, pd)
        # 点击提交
        self.click(self.submitEle)
        INFO('已提交用户名，密码')

