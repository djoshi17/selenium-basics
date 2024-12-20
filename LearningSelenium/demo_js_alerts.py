import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoAlerts:
    def js_alerts(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/")
        driver.maximize_window()
        driver.find_element(By.LINK_TEXT, "JavaScript Alerts").click()
        time.sleep(2)
        # accept alert
        driver.find_element(By.XPATH, "//div[@class='example']//li[1]/button").click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
        #Dismiss alert
        driver.find_element(By.XPATH, "//div[@class='example']//li[2]/button").click()
        time.sleep(2)
        driver.switch_to.alert.dismiss()
        time.sleep(2)
        #send text in alert box
        driver.find_element(By.XPATH, "//div[@class='example']//li[3]/button").click()
        time.sleep(2)
        print(driver.switch_to.alert.text)
        driver.switch_to.alert.send_keys("Mahadev")
        Alert(driver).accept()
        #driver.switch_to.alert.accept()
        time.sleep(4)


testalerts = DemoAlerts()
testalerts.js_alerts()