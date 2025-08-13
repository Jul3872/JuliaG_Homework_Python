from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")

input_field_username = driver.find_element(By.ID, "username")

input_field_username.send_keys("tomsmith")

input_field_password = driver.find_element(By.ID, "password")

input_field_password.send_keys("SuperSecretPassword!")

time.sleep(2)

blue_button = driver.find_element(By.CLASS_NAME, "radius")
blue_button.click()

message = driver.find_element("class name", "flash.success").text
print(message)

driver.quit()
