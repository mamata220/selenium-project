from selenium import webdriver

import time

from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(executable_path="D:\\Selenium\\drivers\\chromedriver.exe")


class Facebook:
    def facebook_login(self):


        driver.get("https://www.facebook.com/")
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='email']").send_keys("srps.us@gmail.com")
        driver.find_element_by_xpath('//*[@id="pass"]').send_keys("Myfbpwd@007")
        driver.find_element_by_xpath('//*[@id="u_0_b"]').click()
        time.sleep(5)
        #driver.find_element_by_xpath('//*[@id="facebook"]/body').send_keys("Hi there")
        driver.find_element_by_xpath(
            "//*[@id='js_52']/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div").click()
        driver.find_element_by_xpath("//*[@id='js_52']/div[1]/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div").send_keys("Hi there by mamata")
        driver.find_element_by_xpath("//*[@id='js_52']/div[2]/div[3]/div[2]/button").click()
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