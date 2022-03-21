from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.browser import Browser


class LoginPageElements(object):
    BODY = '== $0'
    USER = 'user-name'
    USER_SUBMIT = '#identifierNext > content > span'
    PASS = 'password'
    # SUBMIT = '//input[@id='login-button']' LOGIN_ERROR = " //h3[@data-test='error'][contains(.,'Epic sadface:
    # Username and password do not match any user in this service')]"


class LoginPage(Browser):
    # login page actions

    def navigate_to_sauce_lab(self):
        self.driver.get('https://www.saucedemo.com/')

    def get_page_title(self):
        return self.driver.title

    def get_login_error(self):
        return self.driver.find_element_by_xpath(
            "//h3[@data-test='error'][contains(.,'Epic sadface: Username and password do not match any user in this "
            "service')]")

    def get_login_locked_out_error(self):
        return self.driver.find_element_by_xpath("//h3[contains(.,'Epic sadface: Sorry, this user has been "
                                                 "locked out.')]")

    def set_username(self, username):
        user_name_field = self.driver.find_element_by_id(LoginPageElements.USER)
        user_name_field.send_keys(username)

    def set_password(self, password):
        password_field = self.driver.find_element_by_id(LoginPageElements.PASS)
        password_field.send_keys(password)

    def submit_login(self):
        login_btn = self.driver.find_element_by_xpath("//input[@id='login-button']")
        login_btn.click()

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.submit_login()
