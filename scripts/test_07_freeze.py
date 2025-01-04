# ①导包
import time
import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait

from page.freeze_page import FreezePage
from page.home_page import HomePage
from page.login_page import LoginPage
from page.system_page import SystemPage
from utils import DriveUtils, get_alert_text, is_text_present, read_json, get_captcha


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
        self.driver.get("http://test.sunnymoom.top/system/login")
        self.driver.implicitly_wait(2)

    @allure.title("验证未找到需要删除的账号")
    @allure.severity(allure.severity_level.BLOCKER)
    def test07_none_account(self):
        allure.dynamic.title("none_account")
        allure.dynamic.severity("normal")
        with allure.step("测试步骤一：登录后台管理页面，进入学生管理列表，输入需要删除的学号，勾选账号，删除"):
            code = get_captcha(self.driver, 1.25)
            SystemPage().login("admin", "123456", code)
            FreezePage().home_account_button()
            FreezePage().sn("000")
            FreezePage().all_check()
            FreezePage().delete()
            time.sleep(3)
        with allure.step("测试步骤二：断言"):
            is_not = get_alert_text(self.driver, "网络错误!")
            assert is_not

    @allure.title("验证选择多条账号删除的错误")
    @allure.severity(allure.severity_level.BLOCKER)
    def test07_more_account(self):
            allure.dynamic.title("more_account")
            allure.dynamic.severity("normal")
            with allure.step("测试步骤一：登录后台管理页面，进入学生管理列表，输入需要删除的学号，勾选账号，删除"):
                code = get_captcha(self.driver, 1.25)
                SystemPage().login("admin", "123456", code)
                FreezePage().home_account_button()
                FreezePage().sn("")
                FreezePage().all_check()
                FreezePage().delete()
            with allure.step("测试步骤二：断言"):
                is_not =is_text_present(self.driver, "请选择一条数据进行删除！")
                assert is_not

    @allure.title("验证删除成功")
    @allure.severity(allure.severity_level.BLOCKER)
    def test03_delete_suc(self):
            allure.dynamic.title("delete_suc")
            allure.dynamic.severity("normal")
            with allure.step("测试步骤一：登录后台管理页面，进入学生管理列表，输入需要删除的学号，勾选账号，删除"):
                code = get_captcha(self.driver, 1.25)
                time.sleep(1)
                SystemPage().login("admin", "123456", code)
                FreezePage().home_account_button()
                FreezePage().sn("3333")
                FreezePage().check()
                FreezePage().delete()
                time.sleep(2)
            with allure.step("测试步骤二：断言"):
                is_not = is_text_present(self.driver, "学生删除成功!")
                assert is_not