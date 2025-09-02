from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self):
        """Открытие страницы"""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html")

    def set_delay(self, seconds):
        """Установка задержки вычислений"""
        delay_input = self.driver.find_element(By.ID, 'delay')
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, button_text):
        """Нажатие кнопки калькулятора по её текстовому содержимому"""
        button = self.driver.find_element(
            By.XPATH, f"//span[text()='{button_text}']")
        button.click()

    def calculate_expression(self, expression):
        """
        Вычисление выражения (пример: '7+8').

        :param expression: выражение для расчёта ('7+8' или другое)
        """
        for char in expression:
            self.click_button(char)
        self.click_button('=')  # Нажимаем равно

    def get_result(self):
        """Получение результата вычисления"""
        result_element = self.driver.find_element(By.CLASS_NAME, "screen")
        return result_element.text.strip()

    def wait_until_result_is(self, expected_value):
        """Ожидаем пока результат станет равным ожидаемому значению"""
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), str(expected_value))
        )
