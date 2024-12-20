from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(2)
driver.close()