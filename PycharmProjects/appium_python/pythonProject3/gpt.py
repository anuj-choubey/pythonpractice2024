from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.mobileby import MobileBy  # Corrected import
from appium.webdriver.common.options import Options

# Desired capabilities
cap = {
    "platformName": "Android",
    "platformVersion": "13.0",
    "deviceName": "Android Emulator",
    "automationName": "uiautomator2",
    "appPackage": "com.android.chrome",
    "appActivity": "com.google.android.apps.chrome.Main",
}

# Create Appium options
options = Options()

# Start Appium session
driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', options=options, desired_capabilities=cap)
driver.implicitly_wait(10)

# Find elements and perform actions
el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Chrome")
el1.click()
el2 = driver.find_element(by=MobileBy.ID, value="com.android.chrome:id/search_box_text")  # Using MobileBy
el2.send_keys("ccsc.helpersin.com")
el3 = driver.find_element(by=MobileBy.ID, value="com.android.chrome:id/line_2")  # Using MobileBy
el3.click()

# Close the session
driver.quit()
