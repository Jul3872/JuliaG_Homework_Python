# pages/checkout_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_order_details(self, first_name, last_name, postal_code):
        # Ожидание загрузки формы
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )

        # Заполнение формы
        first_name_field = self.driver.find_element(By.ID, "first-name")
        first_name_field.send_keys(first_name)

        last_name_field = self.driver.find_element(By.ID, "last-name")
        last_name_field.send_keys(last_name)

        postal_code_field = self.driver.find_element(By.ID, "postal-code")
        postal_code_field.send_keys(postal_code)

        # Нажатие кнопки Continue
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )
        continue_button.click()

    def get_total_amount(self):
        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")))
        total_text = total_element.text
        total_amount_str = total_text.replace("Total: $", "").strip()
        try:
            total_amount_float = float(total_amount_str)
            return total_amount_float
        except ValueError:
            raise Exception(f"Не удалось преобразовать '{total_amount_str}'"
                            " в число.")
