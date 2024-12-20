import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoFindByElements:
    def find_by_elements(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        lista = driver.find_elements(by=By.TAG_NAME, value="a")
        print(len(lista))
        for i in lista:
            print(i.text)
        driver.maximize_window()
        time.sleep(5)


findbyelements = DemoFindByElements()
findbyelements.find_by_elements()
print("test case pass")