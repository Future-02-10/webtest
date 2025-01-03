# ①导包
import time
import pytest
import allure

from page.home_page import HomePage
from page.login_page import LoginPage
from utils import DriveUtils, get_alert_text, is_text_present, read_json


def teardown_method():
    # ⑤暂停几秒钟
    time.sleep(1)


class TestComment:

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

    # 方法级别后置方法：每个用例执行完成之后，停留2S

    @allure.title("验证未登录无法评论")
    @allure.severity(allure.severity_level.BLOCKER)
    def test01_no_login(self):
        allure.dynamic.title("none_login")
        allure.dynamic.severity("normal")
        with allure.step("测试步骤一：进入商品页面"):
            HomePage().select_goods()
        with allure.step("测试步骤二：断言"):
            is_not = is_text_present(self.driver, "评论总要登录留个名吧")
            assert is_not

    @allure.title("验证空评论")
    @allure.severity(allure.severity_level.BLOCKER)
    def test02_no_comment(self):
        allure.dynamic.title("none_comment")
        allure.dynamic.severity("normal")
        with allure.step("测试步骤一：登录，进入商品页面，不输入评论，点击评论按钮"):
            HomePage().home_to_login()
            LoginPage().login("222", "222")
            HomePage().select_goods("1")
            HomePage().comment("")
        with allure.step("测试步骤二：断言"):
            is_not = get_alert_text(self.driver, "请输入评论内容！")
            assert is_not
        with allure.step("测试步骤三：退出登录"):
            HomePage().logout()

    @allure.title("验证评论成功")
    @allure.severity(allure.severity_level.BLOCKER)
    def test03_comment_suc(self):
        allure.dynamic.title("comment_suc")
        allure.dynamic.severity("normal")
        with allure.step("测试步骤一：登录，进入商品页面，输入评论，点击评论按钮"):
            HomePage().home_to_login()
            LoginPage().login("222", "222")
            HomePage().select_goods("1")
            HomePage().comment("这是一条测试评论")
            time.sleep(1)
        with allure.step("测试步骤二：断言"):
            is_not = get_alert_text(self.driver, "评论成功")
            assert is_not
        with allure.step("测试步骤三：退出登录"):
            HomePage().logout()