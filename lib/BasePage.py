from selenium import webdriver
from common.common import *
import os
import time
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    """
    封装页面的基本方法
    """
    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    # 前进
    def forword(self):
        self.driver.forward()
        INFO("Click forward on current page.")

    # 后退
    def back(self):
        self.driver.back()
        INFO("Click back on current page.")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        INFO("wait for {:d} seconds.".format(seconds))

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            INFO("Closing and quit the browser.")
        except NameError as e:
            ERROR("Failed to quit the browser with %s" % e)

    def get_windows_img(self):
        """
        保存到根目录的Screenshots文件夹下
        """
        file_path = os.getcwd() + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            INFO("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            ERROR("Failed to take screenshot! {0}".format(e))
            self.get_windows_img()

    def find_element(self, by, selector, ele=None):
        """

        :param by: 定位的方法
        :param selector: 方法对应的参数
        :param ele: 节点
        :return: driver
        """
        element = ''
        if ele:
            if by == "i" or by == 'id':
                try:
                    element = ele.find_element_by_id(selector)
                    INFO("Had find the element \' {0} \' successful by {1} via value: {2}"
                         .format(element.text, by, selector))
                except NoSuchElementException as e:
                    ERROR("NoSuchElementException: {}".format(e))
                    self.get_windows_img()  # take screenshot
            elif by == "n" or by == 'name':
                element = ele.find_element_by_name(selector)
            elif by == "c" or by == 'class_name':
                element = ele.find_element_by_class_name(selector)
            elif by == "l" or by == 'link_text':
                element = ele.find_element_by_link_text(selector)
            elif by == "p" or by == 'partial_link_text':
                element = ele.find_element_by_partial_link_text(selector)
            elif by == "t" or by == 'tag_name':
                element = ele.find_element_by_tag_name(selector)
            elif by == "x" or by == 'xpath':
                try:
                    element = ele.find_element_by_xpath(selector)
                    INFO("Had find the element  successful "
                         "by {0} via value: {1} ".format(by, selector))
                except NoSuchElementException as e:
                    ERROR("NoSuchElementException: {}".format(e))
                    self.get_windows_img()
            elif by == "css" or by == 'css_selector':
                try:
                    element = ele.find_element_by_css_selector(selector)
                    INFO("Had find the element \' {0} \' successful "
                         "by {1} via value: {2} ".format(element.text, by, selector))
                except NoSuchElementException as e:
                    ERROR("NoSuchElementException: {}".format(e))
                    self.get_windows_img()
            else:
                raise NameError("Please enter a valid type of targeting elements.")
        else:
            if by == "i" or by == 'id':
                try:
                    element = self.driver.find_element_by_id(selector)
                    INFO("Had find the element \' {0} \' successful by {1} via value: {2}"
                         .format(element.text, by, selector))
                except NoSuchElementException as e:
                    ERROR("NoSuchElementException: {}".format(e))
                    self.get_windows_img()  # take screenshot
            elif by == "n" or by == 'name':
                element = self.driver.find_element_by_name(selector)
            elif by == "c" or by == 'class_name':
                element = self.driver.find_element_by_class_name(selector)
            elif by == "l" or by == 'link_text':
                element = self.driver.find_element_by_link_text(selector)
            elif by == "p" or by == 'partial_link_text':
                element = self.driver.find_element_by_partial_link_text(selector)
            elif by == "t" or by == 'tag_name':
                element = self.driver.find_element_by_tag_name(selector)
            elif by == "x" or by == 'xpath':
                try:
                    element = self.driver.find_element_by_xpath(selector)
                    INFO("Had find the element \' {0} \' successful "
                         "by {1} via value: {2} " .format(element.text, by, selector))
                except NoSuchElementException as e:
                    ERROR("NoSuchElementException: {}".format(e))
                    self.get_windows_img()
            elif by == "css" or by == 'css_selector':
                try:
                    element = self.driver.find_element_by_css_selector(selector)
                    INFO("Had find the element \' {0} \' successful "
                         "by {1} via value: {2} " .format(element.text, by, selector))
                except NoSuchElementException as e:
                    ERROR("NoSuchElementException: {}".format(e))
                    self.get_windows_img()
            else:
                raise NameError("Please enter a valid type of targeting elements.")

        return element

    def find_elements(self, by, selector, ele=None):
        """

        :param by: 定位的方法
        :param selector: 方法对应的参数
        :param ele: 节点
        :return: driver
        """
        elements = ''
        if ele:
            if by == "i" or by == 'id':
                try:
                    elements = ele.find_elements_by_id(selector)
                    INFO("Had find the element  successful by {0} via value: {1}"
                         .format(by, selector))
                except NoSuchElementException as e:
                    ERROR("NoSuchElementException: {}".format(e))
                    self.get_windows_img()  # take screenshot
            elif by == "n" or by == 'name':
                elements = ele.find_elements_by_name(selector)
            elif by == "c" or by == 'class_name':
                elements = ele.find_elements_by_class_name(selector)
            elif by == "l" or by == 'link_text':
                elements = ele.find_elements_by_link_text(selector)
            elif by == "p" or by == 'partial_link_text':
                elements = ele.find_elements_by_partial_link_text(selector)
            elif by == "t" or by == 'tag_name':
                elements = ele.find_elements_by_tag_name(selector)
            elif by == "x" or by == 'xpath':
                try:
                    elements = ele.find_elements_by_xpath(selector)
                    INFO("Had find the elements  successful "
                         "by {0} via value: {1} ".format(by, selector))
                except NoSuchElementException as e:
                    ERROR("NoSuchElementException: {}".format(e))
                    self.get_windows_img()
            elif by == "css" or by == 'css_selector':
                try:
                    elements = ele.find_elements_by_css_selector(selector)
                    INFO("Had find the elements  successful "
                         "by {0} via value: {1} ".format(by, selector))
                except NoSuchElementException as e:
                    ERROR("NoSuchElementException: {}".format(e))
                    self.get_windows_img()
            else:
                raise NameError("Please enter a valid type of targeting elements.")
        else:
            if by == "i" or by == 'id':
                try:
                    elements = self.driver.find_elements_by_id(selector)
                    INFO("Had find the elements  successful by {0} via value: {1}"
                         .format(by, selector))
                except NoSuchElementException as e:
                    ERROR("NoSuchElementException: {}".format(e))
                    self.get_windows_img()  # take screenshot
            elif by == "n" or by == 'name':
                elements = self.driver.find_elements_by_name(selector)
            elif by == "c" or by == 'class_name':
                elements = self.driver.find_elements_by_class_name(selector)
            elif by == "l" or by == 'link_text':
                elements = self.driver.find_elements_by_link_text(selector)
            elif by == "p" or by == 'partial_link_text':
                elements = self.driver.find_elements_by_partial_link_text(selector)
            elif by == "t" or by == 'tag_name':
                elements = self.driver.find_elements_by_tag_name(selector)
            elif by == "x" or by == 'xpath':
                try:
                    elements = self.driver.find_elements_by_xpath(selector)
                    INFO("Had find the elements  successful "
                         "by {0} via value: {1} " .format(by, selector))
                except NoSuchElementException as e:
                    ERROR("NoSuchElementException: {}".format(e))
                    self.get_windows_img()
            elif by == "css" or by == 'css_selector':
                try:
                    elements = self.driver.find_elements_by_css_selector(selector)
                    INFO("Had find the elements  successful "
                         "by {0} via value: {1} " .format(by, selector))
                except NoSuchElementException as e:
                    ERROR("NoSuchElementException: {}".format(e))
                    self.get_windows_img()
            else:
                raise NameError("Please enter a valid type of targeting elements.")

        return elements

    # 输入
    def type(self, ele, text):
        ele.clear()
        try:
            ele.send_keys(text)
            INFO("Had type \' {} \' in inputBox".format(text))
        except NameError as e:
            ERROR("Failed to type in input box with {}".format(e))
            self.get_windows_img()

    # 清除文本框
    def clear(self, ele):
        try:
            ele.clear()
            INFO("Clear text in input box before typing.")
        except NameError as e:
            ERROR("Failed to clear in input box with {}".format(e))
            self.get_windows_img()

    # 点击元素
    @staticmethod
    def click(ele):
        try:
            ele.click()
            logger.info("The element \' {} \' was clicked.".format(ele.text))
        except NameError as e:
            logger.error("Failed to click the element with {}".format(e))

    # 或者网页标题
    def get_page_title(self):
        logger.info("Current page title is {}".format(self.driver.title))
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        INFO("Sleep for {} seconds".format(seconds))

    # 获取元素的文本内容
    @staticmethod
    def getText(ele):
        textList = []
        for i in ele:
            textList.append(i.text)
        return textList
