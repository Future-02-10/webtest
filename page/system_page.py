from selenium.webdriver.common.by import By
from base.base_page import BasePage

class SystemPage(BasePage):
    def __init__(self):
        super().__init__()
        self.user = (By.ID, "username")
        self.pwd = (By.ID, "password")
        self.cpacha = (By.ID, "cpacha")
        self.login_btn = (By.ID,"submit-btn")

    def login(self,user,pwd,cpacha):
        self.input_text(self.find_el(self.user),user)
        self.input_text(self.find_el(self.pwd),pwd)
        self.input_text(self.find_el(self.cpacha), cpacha)
        self.find_el(self.login_btn).click()


if __name__ == '__main__':
    print(SystemPage().user)
    print(*SystemPage().user)