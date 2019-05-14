
import logging
from selenium.common.exceptions import NoSuchElementException
from features.environment import *

# 名称对应到 css selector
NAME2CSS = {
    '资讯收藏': '.icon-collect',
}

# 名称到 xpath 的映射
NAME2XPATH = {
    '评测详情': '//wx-view[@class="news-list"]//wx-view[@class="title"]',
}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s"
)


def get_driver_props(driver):
    """
    获取 driver 常用属性
    """
    return driver.get_window_size()['width'], driver.get_window_size()['height']


def swipe_down(driver, duration=600):
    """
    下拉手势
    :param driver:
    :param duration:
    :return:
    """
    width, height = get_driver_props(driver)
    driver.swipe(width * 0.5, height * 0.25, width * 0.5, height * 0.75, duration=duration)
    return True


def swipe_up(driver, duration=600):
    """
    上滑手势
    :param driver:
    :param duration:
    :return:
    """
    width, height = get_driver_props(driver)
    driver.swipe(width * 0.5, height * 0.75, width * 0.5, height * 0.25, duration=duration)
    return True


def sleep(t):
    time.sleep(t)


def switch_to_context(driver, context='NATIVE'):
    """
    切换上下文，这里可能有多个，需要匹配
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


def switch_to_current_webview_window(driver):
    """
    一个 webview 会有多个窗口，切换到当前激活的窗口
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


def click_applet_from_pulldown(driver, name="有车以后", attr=None):
    """
    从下拉栏点击小程序，暂不支持滑动搜索
    :param driver:
    :param name: 小程序名称
    :param attr: 小程序类型，例如开发版、体验版
    :return:
    """
    if not attr or attr == '正式版':
        xps = "//android.widget.TextView[@text='%s']/../android.widget.FrameLayout[not(android.widget.TextView)]" \
              % name
    else:
        xps = "//android.widget.TextView[@text='%s']/../android.widget.FrameLayout/android.widget.TextView[@text='%s']" \
              % (name, attr)
    try:
        driver.find_element_by_xpath(xps).click()
        return True
    except NoSuchElementException:
        pass
    return False


def is_display_ycyh_native_menu(driver):
    """
    是否有有车以后小程序的底部菜单栏
    :param driver:
    :return:
    """
    try:
        if driver.find_element_by_android_uiautomator('text("资讯")') and \
                driver.find_element_by_android_uiautomator('text("选车")'):
            return True
    except NoSuchElementException:
        pass
    return False


def find_wxapp_target(driver, el):
    """
    查找小程序页面元素
    :param driver:
    :param el:
    :return:
    """
    target = None
    try:
        if NAME2CSS.get(el) or NAME2XPATH.get(el):
            # 切换上下文环境
            if driver.current_context == 'NATIVE_APP':
                switch_to_context(driver, WECHAT_CAPS['chromeOptions']['androidProcess'])
                switch_to_current_webview_window(driver)

            if NAME2CSS.get(el):
                # 通过 css 点击
                css_name = NAME2CSS[el]
                target = driver.find_element_by_css_selector(css_name)
            elif NAME2XPATH.get(el):
                xpath_name = NAME2XPATH[el]
                target = driver.find_element_by_xpath(xpath_name)
        else:
            # 普通文本的点击，先切换上下文环境
            if driver.current_context != 'NATIVE_APP':
                switch_to_context(driver)
            # TODO 这个有时候会命中其他元素
            target = driver.find_element_by_android_uiautomator('text("%s")' % el)
    except NoSuchElementException:
        pass
    return target
