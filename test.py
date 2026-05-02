from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

# 1. ब्राउज़र को रन होने के बाद खुला रखने के लिए
options.add_experimental_option("detach", True)

# 2. YouTube के 'Automation Detection' को चकमा देने के लिए ये सेटिंग्स ज़रूरी हैं
options.add_argument("--disable-blink-features=AutomationControlled") 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 3. एक असली यूजर की तरह दिखने के लिए User-Agent जोड़ें
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)

# 4. 'webdriver' फ्लैग को पूरी तरह से हटाने के लिए यह स्क्रिप्ट चलाएं
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# अब वीडियो लिंक खोलें
driver.get("https://youtu.be/hvqc8lPmCfU?si=5Wz0R0s3RU3Zg5WQ&t=21")
