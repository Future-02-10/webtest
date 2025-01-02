# ①导包
import time
import allure

from page.login_page import LoginPage
from page.home_page import HomePage
from utils import DriveUtils,get_el_text,is_text_present,read_json

class TestHomeLogin:

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
    def teardown_method(self):
        # ⑤暂停几秒钟
        time.sleep(2)

    @allure.title("验证首页登录成功")
    @allure.severity(allure.severity_level.NORMAL)
    def test01_Home_login_suc(self):
        with allure.step("测试步骤一：在首页点击登录按钮，进入登录页面"):
            HomePage().home_to_login()
        with allure.step("测试步骤二：在登录页面输入相关信息，点击登录按钮完成登录"):
            LoginPage().login("111", "111")
        with allure.step("测试步骤三：断言"):
            is_suc=is_text_present(self.driver,"退出")
            assert is_suc
        allure.attach(self.driver.get_screenshot_as_png(),name="登录成功截图",attachment_type=allure.attachment_type.PNG)
