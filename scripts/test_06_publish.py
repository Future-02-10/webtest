# ①导包
import time
import pytest
import allure
from selenium.webdriver.common.by import By

from page.login_page import LoginPage
from page.home_page import HomePage
from page.publish_page import PublishPage
from utils import DriveUtils, get_el_text, is_text_present, read_json, get_alert_text


class TestPublish:

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
        time.sleep(1)

    # 方法级别后置方法：每个用例执行完成之后，停留2S
    def teardown_method(self):
        # ⑤暂停几秒钟
        time.sleep(1)

    # 测试用例：登录功能
    @pytest.mark.parametrize("case_name,upload,name,info,buyPrice,sellPrice,cid,cid2,wait_text",
                             read_json("publish_data"))
    def test01_publish_abnormal(self, case_name, upload, name, info, buyPrice, sellPrice, cid, cid2, wait_text):
        allure.dynamic.title(case_name)
        allure.dynamic.severity("normal")
        with allure.step("测试步骤一：登录，进入我要卖页面，输入信息"):
            HomePage().home_to_login()
            LoginPage().login("333", "333")
            HomePage().home_to_publish()
            self.driver.refresh()
            PublishPage().publish(upload, name, info, buyPrice, sellPrice, cid, cid2)
        with allure.step("测试步骤二：断言"):
            is_not = get_alert_text(self.driver, wait_text)
            assert is_not
        with allure.step("测试步骤三：退出登录"):
            HomePage().logout()

    @allure.title("验证评论成功")
    @allure.severity(allure.severity_level.BLOCKER)
    def test02_publish_suc(self):
        with allure.step("测试步骤一：登录，进入我要卖页面，输入正确的信息"):
            HomePage().home_to_login()
            LoginPage().login("333", "333")
            HomePage().home_to_publish()
            PublishPage().publish("D:\\开发\\webtest\\upload\\test.png", "测试", "一个测试商品,用于测测测测测测测测试", "114", "51", "手机", "智能机")
        with allure.step("测试步骤二：断言"):
            is_not = is_text_present(self.driver, "测试")
            assert is_not
        with allure.step("测试步骤三：退出登录"):
            HomePage().logout()
        allure.attach(self.driver.get_screenshot_as_png(), name="发布成功截图",
                      attachment_type=allure.attachment_type.PNG)
