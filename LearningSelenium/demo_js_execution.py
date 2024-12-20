import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class JSExecution:
    def demo_js_execution(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        #driver.get("https://training.rcvacademy.com/")
        driver.execute_script("window.open('https://training.rcvacademy.com/courses', '_self')")
        time.sleep(8)
        demo_element = driver.execute_script("return document.getElementsByTagName('p')[0];")
        driver.execute_script("arguments[0].click();",demo_element)


demojs = JSExecution()
demojs.demo_js_execution()