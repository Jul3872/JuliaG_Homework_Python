import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_submission_and_validation(driver):
    wait = WebDriverWait(driver, 60)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    wait.until(EC.presence_of_element_located(
        (By.NAME, "first-name"))).send_keys("Иван")
    wait.until(EC.presence_of_element_located(
        (By.NAME, "last-name"))).send_keys("Петров")
    wait.until(EC.presence_of_element_located(
        (By.NAME, "address"))).send_keys("Ленина, 55-3")
    wait.until(EC.presence_of_element_located(
        (By.NAME, "e-mail"))).send_keys("test@skypro.com")
    wait.until(EC.presence_of_element_located(
        (By.NAME, "phone"))).send_keys("+7985899998787")
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@name='zip-code']"))).send_keys("")
    wait.until(EC.presence_of_element_located(
        (By.NAME, "city"))).send_keys("Москва")
    wait.until(EC.presence_of_element_located(
        (By.NAME, "country"))).send_keys("Россия")
    wait.until(EC.presence_of_element_located(
        (By.NAME, "job-position"))).send_keys("QA")
    wait.until(EC.presence_of_element_located(
        (By.NAME, "company"))).send_keys("SkyPro")

    submit_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()

    def check_field_color(field_name, expected_color):
        field = wait.until(EC.presence_of_element_located(
            (By.ID, field_name)))
        color = field.value_of_css_property("border-color")
        assert color == expected_color, (
            f"Field {field_name} has color {color}, expected {expected_color}"
        )
        return color

    check_field_color("zip-code", "rgb(245, 194, 199)")

    green_fields = ["first-name", "last-name", "address", "e-mail", "phone",
                    "city", "country", "job-position", "company"]

    for field_name in green_fields:
        check_field_color(field_name, "rgb(186, 219, 204)")
