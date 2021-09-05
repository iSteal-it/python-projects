import time
from selenium import webdriver

chromedriver: str = "/Users/alyadav/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=chromedriver)

data = driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_id("cookie")


while True:
    for _ in range(5):
        time.sleep(1)
        cookie.click()
    cursor = driver.find_element_by_id("buyCursor")
    grandma = driver.find_element_by_id("buyGrandma")
    factory = driver.find_element_by_id("buyFactory")
    mine = driver.find_element_by_id("buyMine")
    portal = driver.find_element_by_id("buyPortal")
    if portal.get_attribute("class") == "":
        portal.click()
    elif mine.get_attribute("class") == "":
        mine.click()
    elif factory.get_attribute("class") == "":
        factory.click()
    elif grandma.get_attribute("class") == "":
        grandma.click()
    elif cursor.get_attribute("class") == "":
        cursor.click()
