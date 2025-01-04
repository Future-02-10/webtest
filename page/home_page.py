from selenium.webdriver.common.by import By
from base.base_page import BasePage


class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        self.login_button = (By.XPATH, "//*[text()='登录/注册']")
        self.comment_content = (By.XPATH, "//*[@id='comment-content']")
        self.comment_button = (By.XPATH, "//*[@id='submit-comment-btn']")
        self.logout_button = (By.XPATH, "//*[@id='log-btn']")
        self.publish_button = (By.ID, "want-sale")

    def select_goods(self, goods_itme="1"):
        self.find_el((By.XPATH, "/html/body/div[1]/div/div[3]/ul/li[" + goods_itme + "]")).click()

    def home_to_login(self):
        self.find_el(self.login_button).click()

    def home_to_publish(self):
        self.find_el(self.publish_button).click()

    def comment(self, text):
        self.input_text(self.find_el(self.comment_content), text)
        self.find_el(self.comment_button).click()

    def logout(self):
        self.find_el(self.logout_button).click()


if __name__ == '__main__':
    print(HomePage().login_button)
    print(*HomePage().login_button)
