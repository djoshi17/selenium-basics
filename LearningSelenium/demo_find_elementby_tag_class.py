import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoFindByTagAndClassName:
    def find_by_tag_class(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        #driver.find_element(by=By.TAG_NAME,value='input').send_keys("hello@tester.com")
        driver.find_element(by=By.CLASS_NAME, value="email-login-box").send_keys("hi@test.com")
        driver.maximize_window()
        time.sleep(5)


findbytagandclass = DemoFindByTagAndClassName()
findbytagandclass.find_by_tag_class()
print("test case pass")
