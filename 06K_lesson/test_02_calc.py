from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def test_slow_calculator_45_seconds():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 60)

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator."
            "html")

        delay_input = driver.find_element(By.ID, 'delay')
        delay_input.clear()
        delay_input.send_keys("45")

        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        result_element = driver.find_element(By.CLASS_NAME, "screen")
        wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

        assert result_element.text == "15", (
            f"Expected '15', but got '{result_element.text}'"
        )

    finally:
        driver.quit()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
