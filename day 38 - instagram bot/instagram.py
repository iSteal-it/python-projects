import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class Instagram:
    def __init__(self,person):
        self.person = person
        self.email = ""
        self.password = ""
        self.chromedriver: str = ""
        self.driver = webdriver.Chrome(executable_path=self.chromedriver)

    def login_(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        usr = self.driver.find_element_by_name("username")
        usr.send_keys(self.email)
        pwd = self.driver.find_element_by_name("password")
        pwd.send_keys(self.password)
        lgn = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        lgn.click()
        time.sleep(5)
        try:
            cancle =self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
            cancle.click()
        except:
            pass
        time.sleep(15)
        cancle = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
        cancle.click()

    def search(self):
        search = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(self.person)
        time.sleep(3)
        search.send_keys(Keys.RETURN)
        search.send_keys(Keys.ENTER)

    def follow(self):
        time.sleep(3)
        follower_list = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        follower_list.click()
        time.sleep(3)

        followers = self.driver.find_elements_by_class_name('sqdOP')
        for fllwr in followers:
            chk = fllwr.get_attribute("class")
            if "_8A5w5" in chk:
                pass
            else:
                fllwr.click()
