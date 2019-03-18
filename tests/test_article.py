# -*- coding: utf-8 -*-

from wxapp import *
import configs


def test_view_article(driver):
    """
    查看一篇评测文章
    :param driver:
    :param cmdopt:
    :return:
    """
    assert open_wxapp_from_dropdown(driver, name="有车以后")

    # 切换上下文和窗口
    assert switch_to_context(driver, context=configs.ANDROID_CAPS['chromeOptions']['androidProcess'])
    assert switch_to_active_wxapp_window(driver)

    # 进入评测栏目
    driver.find_element_by_xpath('//wx-form[@data-tag="评测"]').click()
    time.sleep(6)
    # TODO 界面元素合理性判断、截图等
    assert True

    # 查看评测文章详情
    driver.find_element_by_xpath('//wx-view[@class="news-list"]//wx-view[@class="title"]').click()
    time.sleep(10)
    # TODO 界面元素合理性判断、截图等
    assert True

    # 这里窗体发生了变化，需要更新
    assert switch_to_active_wxapp_window(driver)

    # 翻页
    scroll_webview_screens(driver, pages=2)
    # TODO 界面元素合理性判断、截图等
    assert True

    time.sleep(3)

    # 评论区，有可能没有评论
    driver.find_element_by_class_name('icon-reply').click()
    time.sleep(3)
    # TODO 界面元素合理性判断、截图等
    assert True

    try:
        # 点击一个用户头像
        driver.find_elements_by_css_selector('.cover.ui-ulogo-default')[1].click()
        time.sleep(6)
        # TODO 界面元素合理性判断、截图等
        assert True
    except (IndexError, WebDriverException):
        pass
