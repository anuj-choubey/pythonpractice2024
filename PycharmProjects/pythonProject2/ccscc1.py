import time

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Any, Dict

# options = AppiumOptions()
cap: Dict[str, Any] = {

    "platformName": "Android",
    "platformVersion": "13.0",
    "deviceName": "emulator-5554",
    "app": "C://Users//Anuj//Downloads//appium-api-demos-3-3-1.apk",
    "automationName": "UIAutomator2",
    "ensureWebviewsHavePages": "True",
    'appPackage': "com.google.android.apps.nexuslauncher",
    'appActivity': ".NexusLauncherActivity",

}
url = 'http://127.0.0.1:4723'
driver = webdriver.Remote('http://127.0.0.1:4723', options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)
print('ok')
driver.press_keycode(4)
print('ok1')

chrome_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable(
        (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.android.chrome:id/search_box_text"]')))
chrome_button.send_keys("ccsc.helpersin.com")

# Wait for the "Register As New User" element and click on it
register_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@content-desc="Register As New User"]'))
)

if register_button.is_displayed():
    register_button.click()

    # Wait for the "Name" element and enter text
    name_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Name\")"))
    )
    name_field.send_keys("tasu bhai")

    # Wait for the "Email" element and enter text
    email_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Email\")"))
    )
    email_field.click()
    email_field.send_keys("tasubhai12@gmail.com")

    # Wait for the "Phone" element and enter text
    phone_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Phone\")"))
    )
    phone_field.send_keys("6261660321")

    # Wait for the "Address" element and enter text
    address_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Address\")"))
    )
    address_field.send_keys("samanpur seth deori sagar ")

    # Wait for the "Aadhar Number" element and enter text
    aadhar_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Aadhar Number\")"))
    )
    aadhar_field.send_keys("359862387742")

    # Wait for the "Password" element and enter text
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Password\")"))
    )
    password_field.send_keys("123")

    # Wait for the "Confirm Password" element and enter text
    confirm_password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Confirm Password\")"))
    )
    confirm_password_field.send_keys("123")

    # Wait for the "Choose File" element and click on it
    # choose_file_button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Choose File"))
    # )
    # choose_file_button.click()

    # Wait for the "Shutter" element and click on it
    # shutter_button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="android:id/icon"])[2]'))
    # )
    # shutter_button.click()

    # Similar waits and interactions for other elements as needed

    # Wait for the "Create Account" element and click on it
    create_account_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Create Account"))
    )
    if create_account_button.is_displayed():
        create_account_button.click()

    time.sleep(20)

# Close the driver session
driver.quit()
