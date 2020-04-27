import configparser
import os.path
from selenium import webdriver
from common.common import *


class Browser:

    def __init__(self):
        self.driver = None
        self.url = None
        self.browserName = None

    def open_browser(self):
        config = configparser.ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
        file_path = os.getcwd() + '/cfg/cfg.ini'
        config.read(file_path, encoding='utf-8')
        # 代码有中文注释，用这个，不然报解码错误

        self.browserName = config.get("browserType", "browserName")
        INFO("You had select {} browser.".format(self.browserName))
        self.url = config.get("testServer", "url")
        INFO("The test server url is: {}".format(self.url))

        if self.browserName == "Firefox":
            self.driver = webdriver.Firefox()
            INFO("Starting firefox browser.")
        elif self.browserName == "Chrome":
            self.driver = webdriver.Chrome()
            INFO("Starting Chrome browser.")
        elif self.browserName == "IE":
            self.driver = webdriver.Ie()
            INFO("Starting IE browser.")
        self.driver.maximize_window()
        INFO("Maximize the current window.")
        self.driver.implicitly_wait(10)
        INFO("Set implicitly wait 10 seconds.")
        GSTORE['getGlobalDriver'] = self.driver

        return self.driver

    def getGlobalDriver(self):
        return GSTORE['getGlobalDriver']


    def openUrl(self, urlPath=''):
        self.driver.get(self.url)
        INFO("Open url: {}".format(self.url+urlPath))

    def quit_browser(self):
        INFO("Now, Close and quit the browser.")
        self.driver.quit()