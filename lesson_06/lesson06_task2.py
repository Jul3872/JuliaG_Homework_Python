from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get('http://uitestingplayground.com/textinput')

driver.find_element(By.ID, 'newButtonName').send_keys('SkyPro')

blu_button = driver.find_element(By.ID, 'updatingButton')
blu_button.click()

wait = WebDriverWait(driver, 20)
wait.until(EC.text_to_be_present_in_element(
    (By.ID, 'updatingButton'), 'SkyPro'))

message = blu_button.text
print(message)

driver.quit()
