
from appium import webdriver
import time
import re

# Appium 服务地址
EXECUTOR = 'http://127.0.0.1:4723/wd/hub'

# Appium 所需的被测手机参数
WECHAT_CAPS = {
    'platformName': 'Android',
    'automationName': 'UIAutomator2',
    'appPackage': 'com.tencent.mm',
    'appActivity': '.ui.LauncherUI',
    'fullReset': False,
    'noReset': True,
    'newCommandTimeout': 7200,
    'platformVersion': '8.0',
    'deviceName': 'b9ee407',
    'chromedriverExecutableDir': '/home/xyz/bin',
    'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'},  # 下拉入口
    'nativeWebScreenshot': True,
}

# Appium 查找一个元素的最大等待时间
IMPLICITLY_WAIT = 10


def before_all(context):
    context.config.setup_logging(level='INFO')


def before_scenario(context, scenario):
    context.driver = webdriver.Remote(EXECUTOR, WECHAT_CAPS)
    context.driver.implicitly_wait(IMPLICITLY_WAIT)
    time.sleep(8)


def after_scenario(context, scenario):
    context.driver.quit()


def after_step(context, step):
    # 每一步执行完毕后判断是否需要等待
    if context.text:
        try:
            sleep_seconds = int(re.search(r'sleep\.(\d+)', context.text).group(1))
            time.sleep(sleep_seconds)
        except:
            pass
