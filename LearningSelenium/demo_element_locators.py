import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoFindElementByID:
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        #driver.find_element(By.ID, "login-input").send_keys("dj@test.com")
        driver.find_element(By.NAME, "login-input").send_keys("hey@tester.com")
        time.sleep(4)


findbyID = DemoFindElementByID()
findbyID.locate_by_id_demo()
print("done")
