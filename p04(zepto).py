from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.maximize_window()
def zepto():
    driver.get("https://www.zepto.com/")
    time.sleep(1)
    searchbar=driver.find_element(By.XPATH,"//a[@aria-label='Search for products']")
    searchbar.click()
    time.sleep(1)
    searchbar02=driver.find_element(By.CSS_SELECTOR,"input[placeholder*='Search for']")
    searchbar02.send_keys("Pears Pure"+Keys.ENTER)
    time.sleep(10)
    shop=driver.find_element(By.XPATH,"//img[@title='Pears Pure & Gentle Bathing Soap']")
    shop.click()
    time.sleep(5)
    addtocart02=driver.find_element(By.XPATH,"(//button[@data-mode='edlp'][normalize-space()='ADD'])[1]")
    addtocart02.click()
    time.sleep(10)
    addtocart=driver.find_element(By.XPATH,"(//button[normalize-space()='Add To Cart'])[1]")
    time.sleep(5)
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});",addtocart)
    addtocart.click()
    time.sleep(5)
    driver.quit()
zepto()
