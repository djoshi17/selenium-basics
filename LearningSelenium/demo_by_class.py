#How to import By class

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoOfByClass:
    def demo_by_class(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.CLASS_NAME, "email-login-box").send_keys("hi@test.com")
        driver.maximize_window()
        time.sleep(4)


demobyclass = DemoOfByClass()
demobyclass.demo_by_class()
print("test case pass")
