from selenium.webdriver.common.by import By
from base.base_page import BasePage

class RegisterPage(BasePage):
    def __init__(self):
        super().__init__()
        self.user = (By.ID, "user-sn")
        self.pwd = (By.ID, "password")
        self.pwd2 = (By.ID, "password2")
        self.qq = (By.ID, "qq")
        self.register_btn = (By.ID,"reg_button")
        self.to_register = (By.ID,"switch_login")

    def register(self,user,pwd,pwd2,qq):
        self.find_el(self.to_register).click()
        self.input_text(self.find_el(self.user),user)
        self.input_text(self.find_el(self.pwd),pwd)
        self.input_text(self.find_el(self.pwd2), pwd2)
        self.input_text(self.find_el(self.qq),qq)
        self.find_el(self.register_btn).click()

if __name__ == '__main__':
    print(RegisterPage().user)
    print(*RegisterPage().user)