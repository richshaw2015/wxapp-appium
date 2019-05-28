# 微信小程序自动化测试——基于Appium&Python3

微信小程序自动化测试方案，基于Appium移动端测试框架及多种测试用例管理框架，使得UI测试更易于实施。

技术方案选型：
1. Appium + Python3 + pytest
2. Appium + Python3 +  behave （BDD风格，推荐）

## 一、背景

在敏捷开发、快速迭代的发布节奏下，需要快速地对小程序、APP等进行回归测试，为了使这一流程标准化、自动化、规范化的执行，本技术方案应运而生。

本项目的开源内容仅限于自动化驱动微信小程序部分，包含了两种技术方案的用例demo，demo基于有车以后小程序，其他业务可自行扩展。

经过有车以后大半年的工程实践检验，该方案比较稳定。通过每天的持续回归测试，累计发现问题10+，效果显著。

## 二、使用教程
### 2.1 开启小程序Web调试
小程序本质上是一种 Web 应用，可以通过PC浏览器进行页面元素的 Inspect。为了进行页面元素的Xpath定位，必须先搞定这一步，参考官方文档：
[【第六季】使用Timeline获取小程序的启动性能数据](https://x5.tencent.com/tbs/guide/debug/season6.html)

> 注意这一步有较多人遇到手机无法开启调试的问题，关键点是要打开腾讯X5的调试开关。可反复尝试下面三个指令（特别是第三个指令），打开相应的开关。

```
http://debugx5.qq.com
http://debugtbs.qq.com
http://debugmm.qq.com/?forcex5=true
```

![](https://github.com/richshaw2015/wxapp-appium/blob/master/img/x5debug.png)

> 如果通过指令 `chrome://inspect/devices#devices` 可以正常看到小程序页面，但是打开后白屏，则需要浏览器设置代理翻墙。直到出现如下界面

![](https://github.com/richshaw2015/wxapp-appium/blob/master/img/inspect.png)

### 2.2 ChromeDriver 下载
Appium 需要通过 chromedriver 驱动微信小程序的webview，遗憾的是微信里面的webview版本号和chromedriver的版本号有一个对应的关系，两者必须要匹配。
微信扫码打开 `http://httpbin.org/user-agent`，即可看到自己的webview版本号（本示例为66）：

```
{
  "user-agent": "Mozilla/5.0 (Linux; Android 7.0; SM-G928V Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044506 Mobile Safari/537.36 MMWEBID/9796 MicroMessenger/7.0.3.1400(0x2700033B) Process/tools NetType/WIFI Language/zh_CN"
}
```
去 [ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads) 找到和自己匹配的 chromedriver 然后下载下来，[历史版本下载地址](https://chromedriver.storage.googleapis.com/index.html)，例如，示例中的66和 `ChromeDriver 2.40` 可以兼容。
```
ChromeDriver 2.40
Supports Chrome v66-68
```
### 2.3 安装[Appium](http://appium.io/)并启动服务
用于驱动手机自动化操作，建议在服务器端运行此服务，运行服务在Mac、Linux上测试通过

需要安装Android SDK、Java等环境，推荐安装最新稳定版

### 2.4 安装Python3及依赖

此脚本仅在 Python3 上测试通过，具体依赖列表参考 `requirements.txt`

推荐安装最新稳定版

### 2.5 修改`configs`/`environment.py`配置
符合自己实际情况即可

### 2.6 运行用例
- 通过 pytest 命令运行：
```
pytest -v -s tests
```

- 通过 behave 命令运行：
```
behave --junit features
```

建议放到 jenkins 上触发执行

## 三、注意事项

### 3.1 微信安全性限制问题
注意尽量不要使用模拟器，应按照正常用户的使用流程，微信的很多功能是有操作频率限制的，一旦使用不当可能面临封号、或者限制使用的风险，所以尽量用小号测试

### 3.2 关于等待时间
涉及到网络的操作或其他异步操作，一般需要显式的等待，根据经验进行调整

### 3.3 异常处理
每一步操作都需要做异常处理，一旦有异常即停止执行，保证后续脚本的执行环境

### 3.4 自动化环境
尽量使用 Mac，特别adb、node这些命令比在Windows下稳定多了

### 3.5 UI用例编写
应根据业务场景，做不同界面的兼容处理

### 3.6 核心门槛
如何从原生的 NATIVE 环境切换到小程序的 Webview 环境，如何在小程序的不同Window切换，详细参考代码实现

### 3.7 测试手机选型
尽量选择接近Android原生系统的手机（对appium的兼容性好），例如 Nexus、三星等，而不是小米、华为这种经过深度定制的，会减少很多莫名其妙的问题及不必要的麻烦

### 3.8 如何切换小程序页面到当前页面？更多问题？
参考源码实现，部分技术未开源，可入群沟通


## 四、微信交流群
请扫码加群，如二维码失效，可加管理员 `richshaw` 申请入群，备注`小程序测试`

![](https://github.com/richshaw2015/wxapp-appium/blob/master/img/qrcode.jpg)

## 五、版权声明
[有车以后](http://youcheyihou.com/)测试组荣誉出品，如果对您项目有帮忙，欢迎Star，开源声明 [The 3-Clause BSD License](https://opensource.org/licenses/BSD-3-Clause) 
