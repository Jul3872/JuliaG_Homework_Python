# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def load(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_credentials(self, username, password):
        user_input = self.driver.find_element(*self.username_field)
        pass_input = self.driver.find_element(*self.password_field)
        user_input.send_keys(username)
        pass_input.send_keys(password)

    def click_login(self):
        btn = self.driver.find_element(*self.login_button)
        btn.click()

    def wait_for_homepage(self):
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/inventory.html"))
