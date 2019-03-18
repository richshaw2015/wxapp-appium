# -*- coding: utf-8 -*-

from wxapp import *
import configs


def test_cal(driver):
    """
    访问计算器页面
    :param driver:
    :return:
    """

    assert open_wxapp_from_dropdown(driver, name="有车以后")

    # 点击计算器栏目，注意这里是在 NATIVE 环境
    driver.find_element_by_android_uiautomator('text("%s")' % '计算器').click()

    time.sleep(10)
    # TODO 界面元素合理性判断、截图等
    assert True

    # 切换到 WEBVIEW 环境
    assert switch_to_context(driver, context=configs.ANDROID_CAPS['chromeOptions']['androidProcess'])
    assert switch_to_active_wxapp_window(driver)

    # 切换到贷款TAB，注意这里实在 WEBVIEW 环境
    driver.find_element_by_xpath("//wx-view[text()='贷款']").click()
    time.sleep(3)

    # TODO 界面元素合理性判断、截图等
    assert True
