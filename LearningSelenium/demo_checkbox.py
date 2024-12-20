import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestCheckBox:
    def demo_checkbox(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//a[@title= 'Non Stop Flights']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@title= 'Student Fare Offer']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@title= 'Armed Forces Offer']").click()
        time.sleep(2)
        var1 = driver.find_element(By.XPATH, "//a[@title= 'Armed Forces Offer']").is_selected()
        print(var1)
        #driver.find_element(By.XPATH, "//a[@title= 'Senior Citizen Offer']").click()
        #time.sleep(3)
        var2 = driver.find_element(By.XPATH, "//a[@title= 'Senior Citizen Offer']").is_selected()
        print(var2)


checkbox = TestCheckBox()
checkbox.demo_checkbox()