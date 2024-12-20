import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class HandleIFrames:
    def demo_iframes(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.maximize_window()
        time.sleep(3)
        #switch with iframe locator
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='iframeResult']"))
        #switch with ID
        driver.switch_to.frame("iframeResult")
        #switch with name
        driver.switch_to.frame("iframeResult")
        #switch with index
        driver.switch_to.frame(0)
        driver.find_element(By.XPATH, "//a[@title='Add HTML Certification']").click()
        time.sleep(5)


iframe = HandleIFrames()
iframe.demo_iframes()