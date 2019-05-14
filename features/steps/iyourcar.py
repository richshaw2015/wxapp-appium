from behave import given, when, then
import random
from features.utils import *


@given("进入{applet}")
def step_impl(context, applet):
    """
    实例： 进入有车以后开发版
    :param context:
    :param applet:
    :return:
    """
    sleep(1)
    swipe_down(context.driver)
    sleep(1)
    open_wxapp_from_dropdown(context.driver, applet)
    sleep(12)
    assert is_display_ycyh_native_menu(context.driver)


@then('翻{num:d}页')
def step_impl(context, num):
    if context.driver.current_context != 'NATIVE_APP':
        switch_to_context(context.driver)
    if num >= 1:
        for i in range(0, num):
            swipe_up(context.driver)
            sleep(1)
    else:
        # 翻半页
        width, height = get_driver_props(context.driver)
        context.driver.swipe(width * 0.5, height * 0.6, width * 0.5, height * 0.25, duration=600)
        sleep(1)


@then('返回')
def step_impl(context):
    if context.driver.current_context != 'NATIVE_APP':
        switch_to_context(context.driver)
    context.driver.back()
    sleep(2)


@when('随机点击文本{els}')
def step_impl(context, els):
    if context.driver.current_context != 'NATIVE_APP':
        switch_to_context(context.driver)
    el = random.choice(els.split('|'))
    context.driver.find_element_by_android_uiautomator('text("%s")' % el).click()
    sleep(1)


@when('点击{el}')
def step_impl(context, el):
    target = find_wxapp_target(context.driver, el)
    target.click()
    sleep(1)


@when("滚动查找{txt}并点击")
def step_impl(context, txt):
    # 自己实现的滑动查找，最多滑动10页
    if context.driver.current_context != 'NATIVE_APP':
        switch_to_context(context.driver)

    width, height = get_driver_props(context.driver)
    starty, endy, startx = height * 0.8, height * 0.2, width / 2
    for i in range(0, 10):
        try:
            context.driver.find_element_by_android_uiautomator('text("%s")' % txt).click()
            return True
        except NoSuchElementException:
            context.driver.swipe(startx, starty, startx, endy, duration=2000)
    logging.warning("滚动查找元素失败：%s", txt)
    return False
