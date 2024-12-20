import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class RightAndDoubleClick:
    def right_double_click(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        #right click
        """achains = ActionChains(driver)
        right_click = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        copyelem = driver.find_element(By.XPATH, "//ul[@class='context-menu-list context-menu-root']/li[3]")
        achains.context_click(right_click).perform()
        time.sleep(3)
        copyelem.click()
        time.sleep(3)"""

        #double click
        achains = ActionChains(driver)
        double_click = driver.find_element(By.XPATH, "//body[@id='authentication']/button")
        achains.double_click(double_click).perform()
        time.sleep(3)


testperform = RightAndDoubleClick()
testperform.right_double_click()