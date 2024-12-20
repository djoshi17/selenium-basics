import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
class DemoFindByCSSSelector():
    def find_by_cssselector(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.CSS_SELECTOR, value="#login-input").send_keys("tester@test.com")
        driver.maximize_window()
        time.sleep(4)


findbycssselector = DemoFindByCSSSelector()
findbycssselector.find_by_cssselector()
print("Test case pass")