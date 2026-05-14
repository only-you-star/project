from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.maximize_window()
def zepto():
    driver.get("https://www.zepto.com/")
    time.sleep(2)
    searchbar=driver.find_element(By.XPATH,"//a[@aria-label='Search for products']")
    searchbar.click()
    time.sleep(3)
    searchbar02=driver.find_element(By.CSS_SELECTOR,"input[placeholder*='Search for']")
    searchbar02.send_keys("Pears Pure"+Keys.ENTER)
    time.sleep(5)
    driver.quit()
zepto()
