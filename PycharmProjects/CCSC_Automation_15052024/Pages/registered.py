import time
from CCSC_Automation_15052024.Base.base_driver import Basedriver


class Register_page_code:

    def __init__(self, driver):
        self.driver = driver
        self.base = Basedriver(driver)
        self.base_url = "https://ccsc.helpersin.com/register/"
        self.register_button_xpath = "//button[contains(text(),'Register As New User')]"
        self.name_input_xpath = "//input[@placeholder='Name']"
        self.email_input_xpath = "//input[@placeholder='Email']"
        self.phone_input_xpath = "//input[@placeholder='Phone']"
        self.address_input_xpath = "//input[@placeholder='Address']"
        self.aadhar_number_input_xpath = "//input[@placeholder='Aadhar Number']"
        self.password_input_xpath = "//input[contains(@name,'password')]"
        self.confirm_password_input_xpath = "//input[@placeholder='Confirm Password']"
        self.choose_file_xpath = "//input[@placeholder='select a file']"
        self.select_category_checkbox_xpath = "//input[@type='checkbox']"
        self.Create_button_xpath = "//button[contains(text(),'Create Account')]"
        self.login_here_button_xpath = "//span[contains(text(),'Login Here')]"
        self.eye_icon1_xpath = "//div[@class ='eye-icon-container']"
        self.eye_icon2_xpath = "//div[@class ='eye-icon-container']"
        self.password_required_field_error_message_field_xpath = "//div[@class = 'Toastify__toast-body']"
        self.password_error_message_xpath = "//div[contains(text(),'Passwords do not match')]"
        self.invalid_mobile_number_error_xpath = "//div[@class = 'Toastify__toast-body']"
        self.email_already_exits_error_message_xpath = "//div[@class = 'Toastify__toast-body']"
        self.register_user = '/html/body/div/div[2]/form/div[3]/div[5]/button'

    def tc11(self):
        self.base.return_any("xpath", self.register_user).click()
        time.sleep(3)
        self.base.return_any("xpath", self.name_input_xpath).clear()
        time.sleep(3)
        self.base.return_any("xpath", self.Create_button_xpath).click()
        time.sleep(10)
