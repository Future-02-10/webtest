import time

from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.user = (By.ID, "login-sn")
        self.pwd = (By.ID, "pwd")
        self.login_btn = (By.ID,"login_button")

    def login(self,user,pwd):
        self.input_text(self.find_el(self.user),user)
        self.input_text(self.find_el(self.pwd),pwd)
        time.sleep(0.5)
        self.find_el(self.login_btn).click()


if __name__ == '__main__':
    print(LoginPage().user)
    print(*LoginPage().user)