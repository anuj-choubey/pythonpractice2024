import time

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "8.1",
    "appium:deviceName": "emulator-5554",
    "appium:app": "C:\\Users\\Anuj\\Downloads\\com-hmh-api-2.apk",
    "appium:automationName": "UIAutomator2",
    "appium:appPackage": "com.google.android.apps.nexuslauncher",
    "appium:appActivity": "com.google.android.apps.nexuslauncher.NexusLauncherActivity",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
driver.press_keycode(4)

# Wait for the element with accessibility ID "Chrome" to be clickable
chrome_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Chrome"]')))

# chrome_button.click()
if chrome_button.is_displayed():
    chrome_button.click()

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
