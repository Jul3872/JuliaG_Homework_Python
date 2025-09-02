import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install()))
    yield driver
    driver.quit()


@pytest.mark.usefixtures("browser")
class TestShopFlow:
    def test_shopping_flow(self, browser):
        login_page = LoginPage(browser)
        main_page = MainPage(browser)
        cart_page = CartPage(browser)
        checkout_page = CheckoutPage(browser)

        # Авторизация
        login_page.load()
        login_page.enter_credentials("standard_user", "secret_sauce")
        login_page.click_login()
        login_page.wait_for_homepage()

        # Добавляем товары в корзину
        main_page.add_items_to_cart()
        main_page.go_to_cart()

        # Переход к оформлению заказа
        cart_page.proceed_to_checkout()

        # Оформляем заказ
        checkout_page.fill_order_details("Юлия", "Галочкина", "680042")

        # Проверяем цену заказа
        total_amount = checkout_page.get_total_amount()
        assert total_amount == 58.29
