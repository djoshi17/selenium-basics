import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class HiddenElement:
    def demo_hidden_element(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        driver.maximize_window()
        demo_displayed = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(demo_displayed)
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "w3-dark-grey").click()
        demo_displayed1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(demo_displayed1)

    def demo_yatra(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/hotels")
        driver.find_element(By.XPATH, "//span[@class='txt-ellipses hotel_passengerBox travellerPaxBox']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//div[@class= 'dflex pax-vol']/div[3]/div/div/span[2]").click()
        time.sleep(3)
        show = driver.find_element(By.CLASS_NAME, "ageselect").is_displayed()
        print(show)
        driver.find_element(By.XPATH, "//div[@class= 'dflex pax-vol']/div[3]/div/div/span[1]").click()
        show1 = driver.find_element(By.CLASS_NAME, "ageselect").is_displayed()
        print(show1)


displayed = HiddenElement()
displayed.demo_yatra()
