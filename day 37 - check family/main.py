from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


email = "rus@isteal.me"
password = ""
chromedriver: str = "/Users/alyadav/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=chromedriver)

data = driver.get("https://www.icloud.com/")

time.sleep(20)

element = driver.find_element_by_class_name("cw-pane-container")
element.click()
