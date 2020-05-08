from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

from selenium.webdriver.support.select import Select



class Facebook:
    def facebook_login(self):
        option = Options()

        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")

        # Pass the argument 1 to allow and 2 to block
        option.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })

        driver = webdriver.Chrome(chrome_options=option, executable_path="D:\\Selenium\\drivers\\chromedriver.exe")

        driver.get("https://www.facebook.com/")
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='email']").send_keys("srps.us@gmail.com")
        driver.find_element_by_xpath('//*[@id="pass"]').send_keys("Myfbpwd@007")
        driver.find_element_by_xpath('//*[@id="u_0_b"]').click()
        time.sleep(5)
        #driver.find_element_by_xpath('//*[@id="facebook"]/body').send_keys("Hi there")
        post_msg_out_div = "/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[2]/div/div/div/form/div[1]/div/div[2]"
        post_msg_out_div_post_msg = "/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[2]/div/div/div/form/div[1]/div/div[2]/textarea"
        #driver.find_element_by_id(post_msg_out_div).click()
        time.sleep(2)
        driver.find_element_by_xpath(post_msg_out_div_post_msg).send_keys("Hi there by mamata")
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/div[2]/button").click()
        time.sleep(8)
        driver.quit()

    """if driver.find_element_by_id("create post").is_displayed():
        drp = Select(driver.find_element_by_id("create post"))
        print(len(drp.options))
        all_options = drp.options
        for options in all_options:
            print(options.text)"""


fb = Facebook()
fb.facebook_login()