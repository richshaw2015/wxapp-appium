
Feature: 资讯详情


  Scenario: 资讯-详情-操作
    Given 进入有车以后
    When 点击评测
      """
      sleep.3
      """
    When 点击评测详情
      """
      sleep.8
      """
    Then 翻2页
    When 点击资讯收藏
      """
      sleep.2
      """
    