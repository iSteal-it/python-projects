from selenium import webdriver
import time

to_check  = [

]

for _ in to_check:
    email = _["apple_id"]
    password = _["password"]

    chromedriver: str = ""
    driver = webdriver.Chrome(executable_path=chromedriver)

    try:
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


        time.sleep(10)
        driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="repairFrame"]'))

        btn = driver.find_element_by_class_name('first')
        btn.click()

        time.sleep(10)

        btn = driver.find_element_by_class_name('first')
        btn.click()

        time.sleep(10)

        driver.switch_to.window(window_now)

        settings = driver.find_element_by_class_name("chevron-view")
        settings.click()

        settings = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div/div[2]/div[1]')
        settings.click()

        time.sleep(10)

        driver.switch_to.frame(driver.find_element_by_id('settings'))

        family = driver.find_elements_by_class_name("family-member")
        driver.close()

        if len(family) >= 1:
            print(f"{email} in family")

        else:
            print(f"{email} no family")

    except :
        print(f"{email} checking error ")
        driver.close()

