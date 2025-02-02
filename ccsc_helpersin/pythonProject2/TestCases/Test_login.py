import time
from ddt import ddt
import pytest
from ccsc_helpersin.pythonProject2.pageObject.userr.Login_page.loginn import Login
from selenium.webdriver.common.alert import Alert
import configparser
from ccsc_helpersin.pythonProject2.Base.email_random import Random

from selenium.webdriver.support.wait import WebDriverWait

config = configparser.ConfigParser()
config.read("C://Users//Anuj//ccsc_helpersin//pythonProject2//Utilities//.properties")


@pytest.mark.usefixtures("setup")
@ddt
class Test_Ccc_Register_Page:
    # def test_without_email_and_password(self):
    #     login = Login(self.driver)
    #     # time.sleep(4)
    #     login.login_button()
    #     time.sleep(4)
    #     login.validate_form()
    #     time.sleep(3)

    # def test_only_email_without_password(self):
    #     login = Login(self.driver)
    #     login.email_login_input(config.get("Credentials","registered_email"))
    #     time.sleep(4)
    #     login.login_button()
    #     time.sleep(4)
    #     login.validate_form()
    #     time.sleep(3)

    # def test_only_password_without_email(self):
    #     login = Login(self.driver)
    #
    #     time.sleep(3)
    #     login.password_login_input(config.get("Credentials","password"))
    #     time.sleep(4)
    #     login.login_button()
    #     time.sleep(4)
    #     login.validate_form()
    #     time.sleep(3)
    #
    # def test_email_and_password_input(self):
    #     login = Login(self.driver)
    #     login.email_login_input(config.get("Credentials", "registered_email"))
    #     time.sleep(4)
    #     login.password_login_input(config.get("Credentials", "password"))
    #     time.sleep(4)
    #     login.login_button()
    #     login.login_successfull_message()
    #     time.sleep(4)

    def test_google_login(self):
        login = Login(self.driver)
        g_email = config.get("Credentials", "g_email")
        g_password = config.get("Credentials", "g_password")
        login.google_login_btn(g_email, g_password)
        time.sleep(20)
        # login.google_input_email(config.get("Credentials","g_email"))
        # time.sleep(10)
