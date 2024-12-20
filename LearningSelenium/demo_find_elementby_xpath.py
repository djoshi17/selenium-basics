import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoFindByXpath:
    def locate_by_xpath(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(by=By.XPATH, value="//input[@id='login-input']").send_keys("tester@test.com")
        driver.maximize_window()
        time.sleep(4)
        driver.close()


findbyxpath = DemoFindByXpath()
findbyxpath.locate_by_xpath()
print("test case pass")