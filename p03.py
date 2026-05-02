from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://www.saucedemo.com")
time.sleep(3)
usern=driver.find_element(By.ID,"user-name")
usern.send_keys("standard_user")
userp=driver.find_element(By.ID,"password")
userp.send_keys("secret_sauce")
logc=driver.find_element(By.NAME,"login-button")
logc.click()
time.sleep(6)
driver.quit()