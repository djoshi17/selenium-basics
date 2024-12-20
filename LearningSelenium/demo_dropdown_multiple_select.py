import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chromeservice
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

class MultiSelect:
    def multiselect_dropdown(self0):
        driver = webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))
        driver.get("http://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
        driver.maximize_window()
        dropdown = driver.find_element(By.XPATH, "//select[@id='multi-select']")
        multi_dropdown = Select(dropdown)

        multi_dropdown.select_by_index(0)
        multi_dropdown.select_by_value("Florida")
        multi_dropdown.select_by_visible_text("New Jersey")
        multi_dropdown.select_by_index(3)
        multi_dropdown.select_by_value("Ohio")
        multi_dropdown.select_by_visible_text("Texas")
        time.sleep(4)
        #multi_dropdown.deselect_by_index(3)
        multi_dropdown.deselect_all()
        time.sleep(5)


multiselect = MultiSelect()
multiselect.multiselect_dropdown()
