from selenium import webdriver
import time

email = ""
password = ""

chromedriver: str = "/Users/alyadav/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=chromedriver)

data = driver.get("https://www.icloud.com/")
window_now = driver.window_handles[0]
time.sleep(10)

driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

email_field = driver.find_element_by_xpath('//*[@id="account_name_text_field"]')
email_field.send_keys(email)

chk = driver.find_element_by_xpath('/html/body/div[3]/apple-auth/div/div[1]/div/sign-in/div/div[1]/button[1]')
chk.click()

time.sleep(5)

password_field = driver.find_element_by_id('password_text_field')
password_field.send_keys(password)

chk = driver.find_element_by_xpath('//*[@id="sign-in"]')
chk.click()

driver.switch_to.window(window_now)

time.sleep(10)
