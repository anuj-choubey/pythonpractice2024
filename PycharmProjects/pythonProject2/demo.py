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
	"appium:app": "C:\\Users\\Anuj\\Downloads\\com-hmh-api-2.apk",
	"appium:automationName": "UIAutomator2",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
    "appium:appPackage":"com.google.android.permissioncontroller",
	"appium:appActivity":"com.android.permissioncontroller.permission.ui.ReviewPermissionsActivity",
	"appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options.load_capabilities(options))

package_name = driver.execute_script('mobile: getCurrentPackage')
desired_caps = driver.desired_capabilities()
el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Chrome")
el1.click()
el2 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.EditText\").instance(0)")
el2.click()
el3 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Register As New User\")")
el3.click()
el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.EditText\").instance(0)")
el4.send_keys("Anuj chobey")
el5 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.EditText\").instance(1)")
el5.send_keys("Anuj123@gmail.com")
el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.EditText\").instance(2)")
el6.click()
el7 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.EditText\").instance(2)")
el7.send_keys("6261660321")
el8 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.EditText\").instance(3)")
el8.send_keys("Bhopal")
el9 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.EditText\").instance(4)")
el9.send_keys("3333445566778899")
el10 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.EditText\").instance(5)")
el10.send_keys("123")
el11 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.EditText\").instance(6)")
el11.send_keys("123")
el12 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
el12.click()
el13 = driver.find_element(by=AppiumBy.ID, value="com.android.permissioncontroller:id/permission_allow_foreground_only_button")
el13.click()
# el14 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"android:id/icon\").instance(1)")
# el14.click()
# el15 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Shutter")
# el15.click()
# el16 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Shutter")
# el16.click()
# el17 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Shutter")
# el17.click()
# el18 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Shutter")
# el18.click()
el19 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
el19.click()
el20 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"android:id/icon\").instance(0)")
el20.click()
el21 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Shutter")
el21.click()
el22 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Done")
el22.click()
el23 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.CheckBox\").instance(0)")
el23.click()
el23.click()
el24 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.CheckBox\").instance(0)")
el24.click()
el25 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.CheckBox\").instance(1)")
el25.click()
el26 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.CheckBox\").instance(2)")
el26.click()
el27 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.CheckBox\").instance(3)")
el27.click()
# el28 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Create Account\")")
# el28.click()
# el28.click()
# el29 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Create Account\")")
# el29.click()
el30 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.CheckBox\").instance(5)")
el30.click()
el31 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Create Account\")")
el31.click()

driver.quit()