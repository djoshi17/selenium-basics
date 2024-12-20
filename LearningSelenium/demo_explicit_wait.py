import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.select import Select

class DemoExplicitWait:
    def demo_exp_wait(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        depart_from.send_keys("New Delhi")
        depart_from.send_keys(Keys.ENTER)
        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.click()
        going_to.send_keys("New York")

        search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_results))
        for result in search_results:
            print(result.text)
            if "New York (JFK)" in result.text:
                result.click()
                break
        wait = WebDriverWait(driver, 10, 2, ignored_exceptions=[StaleElementReferenceException])
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
        #start_date = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        #start_date.click()
        #driver.find_element(By.XPATH, "//td[@id='19/08/2023']").click()

        all_dates = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")))\
                     .find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        #all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == "23/09/2023":
                date.click()
                break
        driver.find_element(By.XPATH, "(//input[@id='BE_flight_flsearch_btn'])[1]").click()


expwait = DemoExplicitWait()
expwait.demo_exp_wait()
print("testcase pass")
