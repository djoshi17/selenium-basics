"""when we comment 4 lines after max window code and run the code we can see the diff output"""


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class WebElementState:
    def check_webelement_state(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://training.openspan.com/login")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//input[@name='user_name']").send_keys("tester")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@name='user_pass']").send_keys("tester123")
        time.sleep(3)
        demo_state = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(demo_state)
        time.sleep(2)


state = WebElementState()
state.check_webelement_state()