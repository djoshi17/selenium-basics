import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoSliders:
    def price_sliders(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.globalsqa.com/demo-site/sliders/#Range")
        driver.maximize_window()
        time.sleep(5)
        driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//iframe[@class='demo-frame lazyloaded']"))
        left_dot = driver.find_element(By.XPATH, "//div[@id='slider-range']/span[1]")
        right_dot = driver.find_element(By.XPATH, "//div[@id='slider-range']/span[2]")
        #ActionChains(driver).drag_and_drop_by_offset(left_dot, 200, 0).perform()
        #ActionChains(driver).click_and_hold(left_dot).pause(1).move_by_offset(50, 0).release().perform()
        #ActionChains(driver).move_to_element(left_dot).pause(1).click_and_hold(left_dot).move_by_offset(80, 0).release().perform()
        ActionChains(driver).drag_and_drop_by_offset(right_dot, -200, 0).perform()
        time.sleep(5)


testsliders = DemoSliders()
testsliders.price_sliders()