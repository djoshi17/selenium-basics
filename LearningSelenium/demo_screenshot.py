import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoScreenshot:
    def capture_screenshot(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        ssdemo = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        ssdemo.screenshot(".\\test.png")
        ssdemo.click()
        time.sleep(3)
        driver.get_screenshot_as_file("c:\\python selenium\\project1\\error.png")
        driver.save_screenshot(".\\test1.png")


sscapture = DemoScreenshot()
sscapture.capture_screenshot()
print("testcase pass...")
