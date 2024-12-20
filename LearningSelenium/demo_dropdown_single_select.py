import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


class DropDownSingleSelect:
    def test_dropdown_single_select(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        dropdown = driver.find_element(By.XPATH, "//select[@name='UserTitle']")
        dd = Select(dropdown)

        dd.select_by_index(1)
        time.sleep(4)

        dd.select_by_value("Marketing_PR_Manager_ANZ")
        time.sleep(4)

        dd.select_by_visible_text("Customer Service Manager")
        time.sleep(4)

testdd = DropDownSingleSelect()
testdd.test_dropdown_single_select()