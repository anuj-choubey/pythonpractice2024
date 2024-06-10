from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap: Dict[Any, str] = {
    "platformName": "Android",
    "platformVersion": "13.0",
    "deviceName": "Android",
    'automationName': "uiautomator2",
    'appPackage': "com.google.android.apps.nexuslauncher",
    'appActivity': ".NexusLauncherActivity",
     'ensureWebviewsHavePages': 'true'

}
url = 'http://127.0.0.1:4723/'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)


el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Chrome")
el1.click()
el2 = driver.find_element(by=AppiumBy.ID, value="com.android.chrome:id/search_box_text")
el2.send_keys("ccsc.helpersin.com")
el3 = driver.find_element(by=AppiumBy.ID, value="com.android.chrome:id/line_2")
el3.click()
