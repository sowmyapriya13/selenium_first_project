from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://localhost:3000/")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "btn-secondary"))
)

time.sleep(3)

increment_element = driver.find_element(By.CLASS_NAME, "btn-secondary" )

for i in range(5):
    increment_element.click()
    time.sleep(1)

reset_element = driver.find_element(By.CLASS_NAME, "btn-primary")
reset_element.click()
time.sleep (2)


delete_element = driver.find_element(By.CLASS_NAME, "btn-danger")

for i in range(2):
    delete_element.click()
    time.sleep(5)

driver.quit()


