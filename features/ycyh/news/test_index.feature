
Feature: 资讯列表


  Scenario: 资讯-列表
    Given 进入有车以后
    When 随机点击文本新闻|导购|用车
      """
      sleep.6
      """
    When 滚动查找热评并点击
      """
      sleep.6
      """
