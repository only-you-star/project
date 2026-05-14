from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
def zepto():
    driver.get("https://www.zepto.com/")
    time.sleep(2)
    driver.quit()
zepto()
