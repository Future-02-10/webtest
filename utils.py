import json
import logging

from selenium import webdriver
from selenium.common import TimeoutException, NoAlertPresentException
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

def get_el_text(driver, xpath_str, wait_text):
    msg = None
    try:
        WebDriverWait(driver, 3, 1).until(
            EC.text_to_be_present_in_element((By.XPATH, xpath_str), wait_text)
        )
    except Exception as e:
        logging.error(e)
        driver.get_screenshot_as_file('执行失败截图.png')
    finally:
        msg = driver.find_element(By.XPATH, xpath_str).text
        logging.info('获取判定的文本信息：{}'.format(msg))
    return msg

def get_alert_text(driver, wait_text, timeout=3):
    msg = None
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: d.switch_to.alert.text == wait_text
        )
        alert = driver.switch_to.alert
        msg = alert.text
        logging.info('获取提示框的文本信息：{}'.format(msg))
        alert.accept()
    except TimeoutException:
        logging.error("等待超时，未找到包含指定文本的提示框。")
        driver.get_screenshot_as_file('执行失败截图.png')
    except NoAlertPresentException:
        logging.error("没有发现提示框。")
        driver.get_screenshot_as_file('执行失败截图.png')
    except Exception as e:
        logging.error(e)
        driver.get_screenshot_as_file('执行失败截图.png')
    finally:
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
