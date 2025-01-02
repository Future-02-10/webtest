import logging.handlers
import os

# 动态获取项目根目录
BASE_PATH = os.path.dirname(__file__)


# 封装初始化日志配置的方法
def init_log_config():
    # 1. 创建日志器对象
    logger = logging.getLogger()
    logger.setLevel("INFO")
    # 2. 创建处理器对象
    #    1. 创建控制台处理器（配置将日志打印到控制台）
    sh = logging.StreamHandler()
    #    2. 创建文件处理器（配置将日志打印到指定的文件夹中）
    # 保存日志的文件地址
    filename = BASE_PATH + "/log/webtest.log"
    fh = logging.handlers.TimedRotatingFileHandler(filename, "midnight", 1, 7, encoding="utf-8")
    # 3. 创建格式化器对象
    # 日志打印格式
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)

    # 4. 将格式化器对象添加到处理器对象中
    #    1. 设置控制台处理器
    sh.setFormatter(formatter)
    #    2. 设置文件处理器
    fh.setFormatter(formatter)

    # 5. 将处理器对象添加到日志器对象中
    #    1. 将控制台处理器添加日志器对象
    logger.addHandler(sh)
    #    2. 将文件处理器添加日志器对象
    logger.addHandler(fh)

