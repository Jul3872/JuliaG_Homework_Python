# pages/main_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_backpack_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.add_bolt_tshirt_btn = (
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.add_onesie_btn = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_items_to_cart(self):
        self.driver.find_element(*self.add_backpack_btn).click()
        self.driver.find_element(*self.add_bolt_tshirt_btn).click()
        self.driver.find_element(*self.add_onesie_btn).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/cart.html"))
