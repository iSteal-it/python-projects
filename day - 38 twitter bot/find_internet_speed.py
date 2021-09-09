from selenium import webdriver
import time

class Speed:
    def __init__(self):
        self.chromedriver: str = ""
        self.driver = webdriver.Chrome(executable_path=self.chromedriver)
    def get_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        click = self.driver.find_element_by_class_name("js-start-test")
        click.click()
        time.sleep(60)

        download_speed = self.driver.find_element_by_class_name("download-speed")
        download_speed = download_speed.text

        upload_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        upload_speed = upload_speed.text
        self.driver.close()
        return [download_speed,upload_speed]
