import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class GetAttributeValue:
    def demo_get_attribute_value(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        attr_value = driver.find_element(By.XPATH, "//input[@value='Search Flights']").get_attribute("class")
        print(attr_value)
        time.sleep(2)


attrobj = GetAttributeValue()
attrobj.demo_get_attribute_value()