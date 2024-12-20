import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class MouseHover:
    def demo_mouse_hover(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        morebutton = driver.find_element(By.XPATH, "//span[@class='more-arr']")
        myaccount = driver.find_element(By.XPATH, "//li[@id='userLoginBlock']/a")
        achains = ActionChains(driver)
        achains.move_to_element(myaccount).perform()
        time.sleep(4)
        achains.move_to_element(morebutton).perform()
        time.sleep(4)
        driver.find_element(By.XPATH, "//span[@class='demo-icon icon-xplore']").click()
        time.sleep(4)


testmouse = MouseHover()
testmouse.demo_mouse_hover()