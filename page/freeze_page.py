import logging
import time
from xml.sax import SAXParseException

from PIL import Image
from PIL import ImageDraw
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sympy.physics.units import action

from base.base_page import BasePage
from selenium.webdriver.common.by import By

class FreezePage(BasePage):
    def __init__(self):
        super().__init__()
        self.account_button = (By.XPATH, "//*[contains(text(), '学生管理')]")
        self.student_list_button = (By.XPATH, "//*[contains(text(), '学生列表')]")
        self.sn_text = (By.NAME, "sn")
        self.search_button = (By.XPATH, "//*[contains(text(), '搜索')]")
        self.one_check = (By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[1]/label")
        self.delete_button = (By.XPATH , "//*[contains(text(), '删除')]")
        self.confirm_delete = (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button[1]")
        self.two_check = (By.XPATH, "/html/body/div/div/main/div/div/div/div/div[2]/div/table/thead/tr/th[1]/label")

    def home_account_button(self):
        self.find_el(self.account_button).click()
        self.find_el(self.student_list_button).click()

    def sn(self, text):
        self.input_text(self.find_el(self.sn_text), text)
        self.find_el(self.search_button).click()

    def all_check(self):
        self.find_el(self.two_check).click()

    def check(self):
        self.find_el(self.one_check).click()

    def delete(self):
        self.find_el(self.delete_button).click()
        time.sleep(2)
        try:
            self.find_el(self.confirm_delete).click()
        except Exception as e:
            logging.error(e)





if __name__ == '__main__':
    print(FreezePage().account_button)
    print(*FreezePage().account_button)
