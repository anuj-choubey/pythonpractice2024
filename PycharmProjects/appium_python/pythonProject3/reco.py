# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "13.0",
    "appium:deviceName": "emulator-5554",
    "appium:app": "C:\\Users\\Anuj\\Downloads\\appium-api-demos-3-3-1.apk",
    "appium:automationName": "UIAutomator2",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
driver.press_keycode(3)
driver.implicitly_wait(100)
el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Chrome")
el1.click()
try:
    el = driver.find_element(by=AppiumBy.ID, value="com.android.chrome:id/search_box_text")
    el.send_keys("ccsc.helpersin.com")
except:
    pass
try:
    el32 = driver.find_element(by=AppiumBy.ID, value="com.android.chrome:id/line_2")
    el32.click()
except:
    pass
el33 = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Register As New User"]')
el33.click()
# actions = ActionChains(driver)
# actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
# actions.w3c_actions.pointer_action.move_to_location(722, 2494)
# actions.w3c_actions.pointer_action.pointer_down()
# actions.w3c_actions.pointer_action.pause(0.1)
# actions.w3c_actions.pointer_action.release()
# actions.perform()

el2 = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="tasu "]')
if el2.is_displayed():
    el2.send_keys("tasu ")
el3 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                          value="new UiSelector().className(\"android.widget.EditText\").instance(1)")
el3.send_keys("tasu7@gmail.com")
# el3.click()
el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                          value="new UiSelector().className(\"android.widget.EditText\").instance(2)")
el4.send_keys("6362616677")
# el4.click()
el5 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                          value="new UiSelector().className(\"android.widget.EditText\").instance(3)")
el5.send_keys("deori ")
# el5.click()
el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                          value="new UiSelector().className(\"android.widget.EditText\").instance(4)")
el6.send_keys("1234567898")
# el6.click()
el7 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                          value="new UiSelector().className(\"android.widget.EditText\").instance(5)")
el7.send_keys("123")
el7 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                          value="new UiSelector().className(\"android.widget.EditText\").instance(6)")
# el7.click()
el8 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                          value="new UiSelector().className(\"android.widget.EditText\").instance(3)")
el8.send_keys("123")
# el8.click()
el9 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
el9.click()
el10 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                           value="new UiSelector().resourceId(\"android:id/icon\").instance(0)")
el10.click()
el11 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Shutter")
el11.click()
el12 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Done")
el12.click()

driver.quit()
