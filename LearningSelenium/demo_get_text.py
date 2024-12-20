import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoOfGetText:
    def demo_get_text(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        text = driver.find_element(By.CLASS_NAME, "main-heading").text
        print(text)
        """driver.get("https://training.rcvacademy.com/")
                text1 = driver.find_element(By.XPATH, "//p[contains(text(),'Curated content and learning roadmaps for people aspiring to get Software Testing/SDET Job or progress in their IT Career!')]").text
                print(text1)"""
        driver.maximize_window()
        time.sleep(4)


gettext = DemoOfGetText()
gettext.demo_get_text()
print("test case pass")
