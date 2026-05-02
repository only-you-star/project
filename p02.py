from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://www.youtube.com")
time.sleep(5)
driver.get("https://youtu.be/hvqc8lPmCfU?si=5Wz0R0s3RU3Zg5WQ&t=21")
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.quit()