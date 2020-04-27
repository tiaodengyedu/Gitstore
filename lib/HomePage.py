from lib.BasePage import BasePage
from common.common import *


class HomePage(BasePage):
    """
    首页
    """
    def __init__(self, driver):
        super().__init__(driver)
        # 定位侧边栏
        self.sider = self.find_element('css', '.sidebar-menu.tree')
        # 定位侧边栏内元素
        self.siderinner = self.find_elements('css', 'span', self.sider)

    def checkLogin(self):
        """
        检查是否登录
        """
        CHECK_POINT('登录检查', self.get_page_title() == '白月销售管理系统')

