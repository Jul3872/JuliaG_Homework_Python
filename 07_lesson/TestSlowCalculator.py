import pytest
from selenium import webdriver
from CalculatorPage import CalculatorPage


class TestSlowCalculator:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.calculator_page = CalculatorPage(self.driver)
        yield
        self.driver.quit()

    def test_slow_calculator_45_seconds(self):
        # Открываем страницу калькулятора
        self.calculator_page.open()

        # Устанавливаем задержку на 45 секунд
        self.calculator_page.set_delay(45)

        # Выполняем расчёт выражния '7 + 8'
        self.calculator_page.calculate_expression("7+8")

        # Ждём, пока результат появится на экране
        self.calculator_page.wait_until_result_is(15)

        # Получаем итоговый результат и сравниваем
        actual_result = int(self.calculator_page.get_result())
        assert actual_result == 15, f"Expected '15', but got {actual_result}"
