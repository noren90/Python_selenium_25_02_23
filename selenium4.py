#Page Object Model
import time

from selenium import webdriver


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field_id = 'user-name'
        self.password_field_id = 'password'
        self.login_button_name = 'login-button'

    def open(self):
        self.driver.get('http://www.saucedemo.com')

    def enter_username(self, username):
        field = self.driver.find_element('id', self.username_field_id)
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.driver.find_element('id', self.password_field_id)
        field.clear()
        field.send_keys(password)

    def click_login(self):
        button = self.driver.find_element('name', self.login_button_name)
        button.click()

driver = webdriver.Chrome()
page1 = LoginPage(driver)
page1.open()
time.sleep(4)
page1.enter_username('standard_user')
page1.enter_password('secret_sauce')
time.sleep(5)
page1.click_login()
time.sleep(10)

