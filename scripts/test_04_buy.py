import time
import pytest
import allure
from page.buy_page import BuyPage
from page.home_page import HomePage
from page.login_page import LoginPage
from utils import DriveUtils, get_alert_text, is_text_present, read_json

class TestBuy:
    # 类级别前置方法：打开浏览器
    def setup_class(self):
        # ②创建浏览器驱动对象
        self.driver = DriveUtils.get_driver()

    # 类级别后置方法：关闭浏览器
    def teardown_class(self):
        # ⑥浏览器驱动对象退出
        DriveUtils.quit_driver()

    # 方法级别前置方法：重新打开页面
    def setup_method(self):
        # ③访问页面
        self.driver.get("http://test.sunnymoom.top/home/index/index")

    @allure.title("验证填写格式不符合")
    @allure.severity(allure.severity_level.BLOCKER)
    def test04_format_enter(self):
        allure.dynamic.title("none_comment")
        allure.dynamic.severity("normal")
        with allure.step("测试步骤一：登录，进入求购页面，输入不完整商品详情，点击发布按钮"):
            HomePage().home_to_login()
            LoginPage().login("222", "222")
            BuyPage().enter_publish()
            BuyPage().buy("苹果手机", "iphone17proMax", "缅甸", "9999")
        with allure.step("测试步骤二：断言"):
            is_not =get_alert_text(self.driver, "详情描述不能少于15个字！")
            assert is_not
        with allure.step("测试步骤三：退出登录"):
            HomePage().logout()

    @allure.title("验证信息未填写完整")
    @allure.severity(allure.severity_level.BLOCKER)
    def test04_no_price(self):
                allure.dynamic.title("none_comment")
                allure.dynamic.severity("normal")
                with allure.step("测试步骤一：登录，进入求购页面，输入不完整信息，点击发布按钮"):
                    HomePage().home_to_login()
                    LoginPage().login("222", "222")
                    BuyPage().enter_publish()
                    BuyPage().buy_enter("苹果手机", "iphone17proMax白色", "缅甸")
                with allure.step("测试步骤二：断言"):
                    is_not = get_alert_text(self.driver, "请填写期望价格")
                    assert is_not
                with allure.step("测试步骤三：退出登录"):
                    HomePage().logout()

    @allure.title("验证发布成功")
    @allure.severity(allure.severity_level.BLOCKER)
    def test04_buy_suc(self):
        allure.dynamic.title("comment_suc")
        allure.dynamic.severity("normal")
        with allure.step("测试步骤一：登录，进入求购页面，输入商品信息，点击发布按钮"):
            HomePage().home_to_login()
            LoginPage().login("222", "222")
            BuyPage().enter_publish()
            BuyPage().buy("苹果手机", "iphone17proMax白色", "缅甸", "9999")
            time.sleep(3)
        with allure.step("测试步骤二：断言"):
            is_suc = is_text_present(self.driver, "退出")
            assert is_suc
        allure.attach(self.driver.get_screenshot_as_png(), name="发布成功截图",
                      attachment_type=allure.attachment_type.PNG)
