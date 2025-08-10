from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/dynamicid")

time.sleep(2)

blue_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary ")
blue_button.click()

time.sleep(5)

driver.quit()
