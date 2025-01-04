import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from utils import DriveUtils


class BasePage:
    def __init__(self):
        self.driver = DriveUtils.get_driver()

    def find_el(self, location_tuple):
        element = None
        try:
            element = WebDriverWait(self.driver, 10, 1). \
                until(lambda x: x.find_element(*location_tuple))
            logging.info("元素{}定位成功".format(location_tuple))
        except:
            logging.info("元素{}定位失败".format(location_tuple))
        return element

    def input_text(self, element, input_text):
        try:
            element.clear()
            element.send_keys(input_text)
            logging.info("输入信息：{}成功".format(input_text))
        except Exception as e:
            logging.info("输入信息：{}失败".format(input_text))
            logging.error(e)

    def select_element(self, element, text):
        try:
            Select(element).select_by_visible_text(text)
            logging.info("选择信息：{}成功".format(text))
        except Exception as e:
            logging.info("选择信息：{}失败".format(text))
            logging.error(e)
