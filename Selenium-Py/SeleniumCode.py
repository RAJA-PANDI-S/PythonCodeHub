from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Open sample login website
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

# Enter username
driver.find_element(By.ID, "username").send_keys("tomsmith")

# Enter password
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
time.sleep(3)

# Click Login
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(3)

# Verify login
if "You logged into a secure area!" in driver.page_source:
    print("Login Successful")
else:
    print("Login Failed")

driver.quit()