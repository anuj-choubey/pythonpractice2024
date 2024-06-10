from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "8.1",
    "appium:deviceName": "emulator-5554",
    "appium:app": "C:\\Users\\Anuj\\Downloads\\com-hmh-api-2.apk",
    "appium:automationName": "UIAutomator2",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# Simulate pressing the back button before finding the "Sign In" element
driver.press_keycode(4)

try:
    # Wait for "Sign In" element to be visible
    el1 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Sign In')))
    el1.click()
except TimeoutException:
    print("Element 'Sign In' not found within 10 seconds.")

try:
    # Wait for "Username" element to be clickable
    el2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("username")')))
    el2.click()
except TimeoutException:
    print("Element 'Username' not clickable within 10 seconds.")

try:
    # Wait for "Password" element to be clickable
    el4 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("password")')))
    el4.click()
except TimeoutException:
    print("Element 'Password' not clickable within 10 seconds.")

try:
    # Wait for "Login" element to be clickable
    el6 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Login')))
    el6.click()
except TimeoutException:
    print("Element 'Login' not clickable within 10 seconds.")

try:
    # Wait for "Image" element to be clickable
    el7 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Image')))
    el7.click()
except TimeoutException:
    print("Element 'Image' not clickable within 10 seconds.")

driver.quit()
