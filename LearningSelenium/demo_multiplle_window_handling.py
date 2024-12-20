import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class MultipleWindowHandle:
    def multi_window(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        parent_handle = driver.current_window_handle
        print(parent_handle)
        #driver.find_element(By.XPATH, "//img[@class='conta iner']").click()
        driver.find_element(By.XPATH, "//a[@id='booking_engine_visa']").click()
        all_handles = driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                driver.find_element(By.XPATH, "//img[@alt='InduInd Visa Travel Card']").click()
                time.sleep(5)
                driver.close()
                time.sleep(5)
                break

        driver.switch_to.window(parent_handle)
        driver.find_element(By.XPATH, "//a[@id='booking_engine_visa']").click()
        time.sleep(4)




demomulti = MultipleWindowHandle()
demomulti.multi_window()

#driver.find_element(By.XPATH, "//button[@class = 'secondarySubscribeButton font-regular-16  banner-button']").click()
#driver.find_element(By.XPATH, "//img[@class='conta iner']").click()