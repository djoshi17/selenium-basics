import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoDragDrop:
    def drag_and_drop(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://demo.guru99.com/test/drag_drop.html")
        driver.maximize_window()
        elem1 = driver.find_element(By.XPATH, "//div[@id='products']//li[2]")
        elem2 = driver.find_element(By.XPATH, "//ol[@id='amt7']")
        #ActionChains(driver).drag_and_drop(elem1,elem2).perform()
        ActionChains(driver).drag_and_drop_by_offset(elem1, 300, 50).perform()
        time.sleep(5)


testdemo = DemoDragDrop()
testdemo.drag_and_drop()
print("testcase pass")
