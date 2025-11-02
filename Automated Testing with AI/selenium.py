from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# initialize browser 
driver = webdriver.Chrome()

# open login page 
driver.get("https://academy.powerlearnprojectafrica.org/login")

# valid credentials
username = "aguerowaza@gmail.com"
password = "Erick@#20"

driver.find_element(By.ID, "email").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "button").click()  
time.sleep(5)  # wait for login to complete


# verify login by checking for a specific element on the landing page
try:
    dashboard_element = driver.find_element(By.XPATH, "//h1[contains(text(), 'Dashboard')]")
    print("Login successful, Dashboard found.")
except:
    print("Login failed, Dashboard not found.") 
finally:
    driver.quit()  # close the browser  

    
