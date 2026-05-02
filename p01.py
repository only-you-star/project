from selenium import webdriver
# import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options=Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get("https://youtu.be/hvqc8lPmCfU?si=5Wz0R0s3RU3Zg5WQ&t=21")

# time.sleep(100)