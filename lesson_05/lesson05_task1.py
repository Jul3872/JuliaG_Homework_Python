from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")

blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
blue_button.click()

sleep(5)

driver.quit()
