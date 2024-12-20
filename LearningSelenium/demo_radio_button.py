import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestRadioButton:
    def demo_radio_button(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.globalsqa.com/samplepagetest/")
        driver.maximize_window()
        #driver.find_element(By.XPATH, "//input[@value='Graduate']").click()
        #time.sleep(5)
        testradio = driver.find_element(By.XPATH, "//input[@value='Graduate']").is_selected()
        print(testradio)
        time.sleep(5)
        driver.find_element(By.XPATH, "//input[@value='Post Graduate']").click()
        time.sleep(5)
        testradio1 = driver.find_element(By.XPATH, "//input[@value='Post Graduate']").is_selected()
        print(testradio1)
        time.sleep(5)


radiobutton = TestRadioButton()
radiobutton.demo_radio_button()


"""
driver.get("https://www.yatra.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//span[@class='txt-ellipses flight_passengerBox travellerPaxBox']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//div[@id='flight_class_select_child']/ul/li[1]/span").is_selected()
        time.sleep(5)
        radio = driver.find_element(By.XPATH, "//div[@id='flight_class_select_child']/ul/li[1]/span").is_selected()
        print(radio)
        time.sleep(3)
        driver.find_element(By.XPATH, "//div[@id='flight_class_select_child']/ul/li[2]/span").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//div[@id='flight_class_select_child']/ul/li[3]/span").click()
        time.sleep(5)
        radio1 = driver.find_element(By.XPATH, "//div[@id='flight_class_select_child']/ul/li[3]/span").is_selected()
        print(radio1)
"""