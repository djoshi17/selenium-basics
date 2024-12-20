import time
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoFindByLinkText:
    def find_by_link_text(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(by=By.LINK_TEXT, value=" Yatra for Business ").click()
        #driver.find_element(by=By.PARTIAL_LINK_TEXT, value=" Yatra for").click()


findbylinktext = DemoFindByLinkText()
findbylinktext.find_by_link_text()
print("testcase pass")
