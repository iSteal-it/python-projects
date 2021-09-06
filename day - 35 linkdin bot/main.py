from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
linkdin_email = "akwebguide@gmail.com"
linkdin_password = "Krevory123@"
PHONE = "6264147206"

chromedriver: str = "/Users/alyadav/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=chromedriver)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

time.sleep(3)

sign_in = driver.find_element_by_class_name("nav__button-secondary")
sign_in.click()

time.sleep(3)

usr = driver.find_element_by_name("session_key")
usr.send_keys(linkdin_email)

password = driver.find_element_by_name("session_password")
password.send_keys(linkdin_password)

sign_in_to = driver.find_element_by_class_name("btn__primary--large")
sign_in_to.click()

time.sleep(3)
try:
    apply_now = driver.find_element_by_class_name("jobs-apply-button")
    apply_now.click()

    phone = driver.find_element_by_class_name("fb-single-line-text__input")
    phone.send_keys(PHONE)

    submit = driver.find_element_by_css_selector("footer button")
    submit.click()
except NoSuchElementException:
    pass
