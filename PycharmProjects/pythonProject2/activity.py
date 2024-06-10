from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Any, Dict

options = AppiumOptions()
cap: Dict[str, Any] = {

    "platformName": "Android",
    "appium:platformVersion": "8.1",
    "appium:deviceName": "emulator-5554",
    "appium:app": "C:\\Users\\Anuj\\Downloads\\com-hmh-api-2.apk",
    "appium:automationName": "UIAutomator2",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True,
    "appium:noRecet": True
}

url = 'http://localhost:4724'
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.press_keycode(4)

try:
    # Wait for the element with accessibility ID "Chrome" to be clickable
    chrome_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Chrome"]'))
    )
    chrome_button.click()

    # Wait for the "Register As New User" element and click on it
    register_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Register As New User\")"))
    )
    register_button.click()

    # Wait for the "Name" element and enter text
    name_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Name\")"))
    )
    name_field.send_keys("tasu bhai")

    # Similar waits and interactions for other elements as needed

    # Wait for the "Create Account" element and click on it
    create_account_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Create Account"))
    )
    create_account_button.click()

except TimeoutException as e:
    print("Timeout occurred while waiting for an element:", e)

finally:
    # Close the driver session
    driver.quit()
