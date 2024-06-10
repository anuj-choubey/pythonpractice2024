from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap: Dict[Any, str] = {
    "platformName": "Android",
    "platformVersion": "13.0",
    "deviceName": "Android",
    'automationName': "uiautomator2",
    'appPackage': "",
    'appActivity': "",

}
url = 'http://127.0.0.1:4724'

driver = webdriver.Remote(url,options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)


