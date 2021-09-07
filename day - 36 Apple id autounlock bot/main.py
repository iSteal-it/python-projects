from selenium import webdriver
import time

to_check = [

]

for check in to_check:
    mail = check["apple_id"]
    apple_pass = check["password"]

    chromedriver: str = ""
    driver = webdriver.Chrome(executable_path=chromedriver)

    driver.get("https://iforgot.apple.com/password/verify/appleid")


    forgot = driver.find_element_by_class_name("generic-input-field")
    time.sleep(5)
    forgot.send_keys(mail)

    continue_button = driver.find_element_by_class_name("button")
    continue_button.click()

    time.sleep(5)

    unlock_seq = False
    try:
        is_lock = driver.find_element_by_class_name("subtitle")
        if(is_lock.text) == "Select how you want to unlock your account:":
                send_unlock_mail = driver.find_element_by_id("action")
                send_unlock_mail.click()
                unlock_seq = True
        else:
            print(f"{mail} ID not lock")
    except:
        print(f"{mail} apple id error check apple id")

    if unlock_seq:
        driver2 = webdriver.Chrome(executable_path=chromedriver)
        driver2.get("https://mail.hostinger.com/")

        time.sleep(5)
        user_name = driver2.find_element_by_name("_user")
        user_name.send_keys(mail)

        pass_word = driver2.find_element_by_name("_pass")
        pass_word.send_keys("")

        login_button = driver2.find_element_by_id("rcmloginsubmit")
        login_button.click()

        mail_search = driver2.find_element_by_name("_q")
        mail_search.send_keys("apple")

        time.sleep(5)

        show_unread_message = driver2.find_element_by_xpath("//a[@title='Show unread messages']")
        show_unread_message.click()
        show_unread_message.click()


        time.sleep(3)

        select_message = driver2.find_element_by_class_name("message")
        select_message.click()
        select_message.click()

        time.sleep(3)

        iforgot_url = driver2.find_element_by_css_selector("p a")
        unlock_url = iforgot_url.get_attribute("href")


        driver3 = webdriver.Chrome(executable_path=chromedriver)
        driver3.get(unlock_url)

        unlock_button = driver3.find_element_by_class_name("unlock")
        unlock_button.click()

        time.sleep(3)

        enter_password = driver3.find_element_by_class_name("generic-input-field")
        enter_password.send_keys(apple_pass)

        unlck = driver3.find_element_by_class_name("right-nav")
        unlck.click()
        print(f"{mail} apple id unlocked")
