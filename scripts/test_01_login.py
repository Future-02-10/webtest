# ①导包
import time
import pytest
import allure

from page.login_page import LoginPage
from utils import DriveUtils,get_el_text,is_text_present,read_json

class TestLogin:

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
        self.driver.get("http://test.sunnymoom.top/home/index/login")
        time.sleep(1)

    # 方法级别后置方法：每个用例执行完成之后，停留2S
    def teardown_method(self):
        # ⑤暂停几秒钟
        time.sleep(1)

    # 测试用例：登录功能
    @pytest.mark.parametrize("case_name,user,pwd,exp_el,expect",read_json("login_data"))
    def test01_login_abnormal(self,case_name,user,pwd,exp_el,expect):
        allure.dynamic.title(case_name)
        allure.dynamic.severity("normal")
        with allure.step("测试步骤一：输入用户名、密码，点击登录"):
            LoginPage().login(user,pwd)
        with allure.step("测试步骤二：断言"):
            msg=get_el_text(self.driver,exp_el,expect)
            assert expect in msg

    @allure.title("验证登录成功")
    @allure.severity(allure.severity_level.BLOCKER)
    def test02_login_suc(self):
        with allure.step("测试步骤一：输入正确的用户名、密码，点击登录"):
            LoginPage().login("111","111")
        with allure.step("测试步骤二：断言"):
            is_suc=is_text_present(self.driver,"退出")
            assert is_suc
        allure.attach(self.driver.get_screenshot_as_png(),name="登录成功截图",attachment_type=allure.attachment_type.PNG)
