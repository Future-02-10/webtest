from selenium.webdriver.common.by import By
from base.base_page import BasePage

class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        self.login_button=(By.XPATH,"//*[text()='登录/注册']")

    def home_to_login(self):
        self.find_el(self.login_button).click()

if __name__ == '__main__':
    print(HomePage().login_button)
    print(*HomePage().login_button)