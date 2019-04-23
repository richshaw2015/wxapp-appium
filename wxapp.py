# -*- coding: utf-8 -*-

import logging
import time
from selenium.common.exceptions import NoSuchElementException, WebDriverException

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s"
)


def swipe_down(driver):
    """
    下拉手势，需要在 NATIVE 环境执行
    :param driver:
    :return:
    """
    width, height = driver.get_window_size()['width'], driver.get_window_size()['height']
    driver.swipe(width * 0.5, height * 0.25, width * 0.5, height * 0.75, duration=800)
    return True


def switch_to_context(driver, context='NATIVE'):
    """
    切换上下文，这里可能有多个，需要匹配，例如 NATIVE_APP、WEBVIEW_com.tencent.mm:tools、WEBVIEW_com.tencent.mm:appbrand0
    :param driver:
    :param context: 取值 WEBVIEW 、NATIVE
    :return: 切换成功返回 True
    """
    contexts = driver.contexts
    for cnt in contexts:
        if context in cnt:
            driver.switch_to.context(cnt)
            logging.debug("切换到：%s", cnt)
            return True
    return False


def switch_to_active_wxapp_window(driver):
    """
    一个 webview 会有多个窗口对象（每个窗口对应一个小程序页面），切换到当前激活的窗口。需要在 WEBVIEW 环境执行
    :param driver:
    :return: 切换成功返回 True
    """
    windows = driver.window_handles

    for window in windows:
        driver.switch_to.window(window)
        if ':VISIBLE' in driver.title:
            logging.debug("切换到窗口：%s", driver.title)
            return True
    return False


def scroll_webview_screens(driver, pages=1, direction='down'):
    """
    向下滑动指定的页数，每次滑动一个可见的滑动区域范围。需要在 WEBVIEW 环境执行
    :param driver:
    :param pages:
    :param direction: 滑动方向，默认往下滑动
    :return:
    """
    for i in range(0, pages):
        # TODO 这个滑动的距离需要结合手机调试确定
        if direction == 'down':
            driver.execute_script("window.scrollBy(0, window.screen.availHeight - 170)")
        elif direction == 'up':
            driver.execute_script("window.scrollBy(0, 170 - window.screen.availHeight)")
        time.sleep(0.5)


def open_wxapp_from_dropdown(driver, name, attr=''):
    """
    从微信顶部下拉栏进入小程序，需要在 NATIVE 环境执行
    :param driver:
    :param name: 小程序名称，如有车以后
    :param attr: 小程序类型，例如开发版、体验版、正式版
    :return:
    """
    try:
        # 等待微信被启动
        time.sleep(6)
        swipe_down(driver)
        time.sleep(1)

        if not attr or attr == '正式版':
            xpath = "//android.widget.TextView[@text='%s']/../android.widget.FrameLayout[not(android.widget.TextView)]" \
                  % name
        else:
            xpath = "//android.widget.TextView[@text='%s']/../android.widget.FrameLayout/android.widget.TextView[@text='%s']" \
                  % (name, attr)
        driver.find_element_by_xpath(xpath).click()

        # 点击后要等待小程序加载
        time.sleep(10)
        # TODO 界面元素校验，是否成功加载了目标小程序
        return True
    except NoSuchElementException:
        return False
