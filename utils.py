import json
import logging

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from config import BASE_PATH



class DriveUtils:
    __driver = None

    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            cls.__driver = webdriver.Edge()
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(10)
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        if cls.__driver is not None:
            cls.__driver.quit()
            cls.__driver = None


def get_el_text(driver,xpath_str,wait_text):
    msg = None
    try:
        WebDriverWait(driver,3,1).until(
            EC.text_to_be_present_in_element((By.XPATH,xpath_str),wait_text)
        )
    except Exception as e:
        print(e)
        driver.get_screenshot_as_file('执行失败截图.png')
    finally:
        msg = driver.find_element(By.XPATH,xpath_str).text
        print('获取判定登录的文本信息：{}'.format(msg))
    return msg

def is_text_present(driver, text):
    try:
        WebDriverWait(driver, 3, 1).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '{}')]".format(text)))
        )
        return True
    except TimeoutException as e:
        print(e)
        driver.get_screenshot_as_file('执行失败截图.png')
        return False

def read_json(filename):
    file_path = BASE_PATH + '/data/{}.json'.format(filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        all_case = json.load(f)
    logging.info("获取原始外部文件测试数据：{}".format(all_case))
    case_list = list()
    for case_dict in all_case.values():
        case_tule = tuple(case_dict.values())
        case_list.append(case_tule)
    logging.info("转化后的测试数据：{}".format(case_list))
    return case_list
