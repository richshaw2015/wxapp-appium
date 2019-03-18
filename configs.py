
# Appium 服务地址 TODO 根据实际情况修改
EXECUTOR = 'http://192.168.0.244:4723/wd/hub'

# Appium 所需的被测手机参数，TODO 需要根据实际情况修改 platformVersion、deviceName、chromedriverExecutableDir
ANDROID_CAPS = {
    'platformName': 'Android',
    'automationName': 'UIAutomator2',
    'appPackage': 'com.tencent.mm',
    'appActivity': '.ui.LauncherUI',
    'fullReset': False,
    'noReset': True,
    'newCommandTimeout': 7200,
    'platformVersion': '7.0',
    'deviceName': '0915f911a8d02504',
    'chromedriverExecutableDir': '/Users/yons/bin',
    'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'},  # 下拉入口
    'nativeWebScreenshot': True,
}

# Appium 查找一个元素的最大等待时间
IMPLICITLY_WAIT = 10
