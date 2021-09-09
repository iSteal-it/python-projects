import time

from selenium import webdriver
import time

class Twitter:
    def __init__(self):
        self.chromedriver: str = "/Users/alyadav/Desktop/chromedriver"
        self.driver = webdriver.Chrome(executable_path=self.chromedriver)
    def login_(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(5)
        user_ = self.driver.find_element_by_name("session[username_or_email]")
        user_.send_keys("istealv6@gmail.com")

        pass_ = self.driver.find_element_by_name("session[password]")
        pass_.send_keys("Alyadav1@")

        login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
        login.click()

    def tweet(self,speed,speeds):
        time.sleep(5)
        tweet_txt = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_txt.send_keys(f"my download speed {speed}\n my upload speed {speeds}")

        send = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        send.click()