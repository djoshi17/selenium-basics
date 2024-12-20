import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.select import Select


class ImplicitWait:
    def demo_implicit_wait(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(10)
        driver.get("https://login.salesforce.com/?locale=in")
        driver.find_element(By.ID, "username").send_keys("darshana")
        driver.find_element(By.ID, "password").send_keys("darshana")


impwait = ImplicitWait()
impwait.demo_implicit_wait()
