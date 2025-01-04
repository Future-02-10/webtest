import time
import logging

from selenium.webdriver.common.by import By
from base.base_page import BasePage


class PublishPage(BasePage):
    def __init__(self):
        super().__init__()
        self.upload = (By.XPATH, '//*[@id="uploadFile"]')
        self.name = (By.XPATH, '//*[@id="name"]')
        self.info = (By.XPATH, '//*[@id="desc"]')
        self.buyPrice = (By.XPATH, '//*[@id="buyPrice"]')
        self.sellPrice = (By.XPATH, '//*[@id="sellPrice"]')
        self.cid = (By.XPATH, '//*[@id="cid"]')
        self.cid2 = (By.XPATH, '//*[@id="cid2"]')
        self.submit = (By.XPATH, '//*[@id="submit-btn"]')

    def publish(self, file_path, name, info, buyPrice, sellPrice, cid, cid2):
        self.input_text(self.find_el(self.upload), file_path)
        self.input_text(self.find_el(self.name), name)
        self.input_text(self.find_el(self.info), info)
        self.input_text(self.find_el(self.buyPrice), buyPrice)
        self.input_text(self.find_el(self.sellPrice), sellPrice)
        self.select_element(self.find_el(self.cid), cid)
        self.select_element(self.find_el(self.cid2), cid2)
        self.find_el(self.submit).click()


if __name__ == '__main__':
    print(PublishPage().name)
    print(*PublishPage().name)
