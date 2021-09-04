from selenium import webdriver

chromedriver: str = "/Users/alyadav/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=chromedriver)

data = driver.get("https://www.amazon.in/")

driver.quit()
