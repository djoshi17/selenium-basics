import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

"""
#Navigate to: driver.get("https://training.rcvacademy.com")
#Get Current URL: driver.current_url
#Back: driver.back()
#Forward: driver.forward()
#Refresh Page: driver.refresh()
#Get Page Title: driver.title
#Maximize Window: driver.maximize_window()
#Minimize Window: driver.minimize_window()
#Full screen window: driver.fullscreen_window()
#Closing a window or tab: driver.close()
#Quitting the browser at the end of a session: driver.quit()"""


class DemoBrowserMethods:
    def browser_methods_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://training.rcvacademy.com")
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        driver.fullscreen_window()
        driver.refresh()
        driver.find_element(By.LINK_TEXT, "ALL COURSES").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(2)
        driver.minimize_window()
        time.sleep(4)
        driver.quit()


demoBM = DemoBrowserMethods()
demoBM.browser_methods_demo()
print("test case pass")