from selenium.webdriver.common.by import By
from base.base_page import BasePage
class BuyPage(BasePage):
    def __init__(self):
        super().__init__()
        self.publish_button = (By.ID,"submit-btn")
        self.name = (By.XPATH,"//*[@id='name']")
        self.desc = (By.XPATH,"//*[@id='desc']")
        self.place = (By.XPATH,"//*[@id='tradePlace']")
        self.price = (By.XPATH,"//*[@id='sellPrice']")

    def enter_publish(self):
        self.find_el((By.ID,"want-buy")).click()

    def buy(self, name, desc, place, price):
        self.input_text(self.find_el(self.name), name)
        self.input_text(self.find_el(self.desc), desc)
        self.input_text(self.find_el(self.place), place)
        self.input_text(self.find_el(self.price), price)
        self.find_el(self.publish_button).click()
if __name__ == '__main__':
    print(BuyPage().publish_button)
    print(*BuyPage().publish_button)