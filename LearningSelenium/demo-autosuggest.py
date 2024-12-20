import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.select import Select


class DemoAutoSuggest:
    def demo_autosuggest_dropdown(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.maximize_window()

        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        time.sleep(4)
        depart_from.send_keys("New Delhi")
        time.sleep(4)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(4)

        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
        time.sleep(4)

        search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_results))

        for result in search_results:
            print(result.text)
            if "New York (JFK)" in result.text:
                result.click()
                time.sleep(4)
                break

        start_date = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        start_date.click()
        time.sleep(4)
        """driver.find_element(By.XPATH, "//td[@id='19/08/2023']").click()
        time.sleep(4)"""

        all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == "23/09/2023":
                date.click()
                break

autosuggestion = DemoAutoSuggest()
autosuggestion.demo_autosuggest_dropdown()
print("testcase pass")
