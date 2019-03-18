# coding: utf-8

import pytest
import configs
from appium import webdriver


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    """
    每个用例初始化一个 WebDriver 对象；回话结束时销毁
    """
    driver = webdriver.Remote(configs.EXECUTOR, configs.ANDROID_CAPS)
    # 查找一个元素的最大等待时间
    driver.implicitly_wait(configs.IMPLICITLY_WAIT)
    yield driver
    driver.quit()
