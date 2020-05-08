from selenium import webdriver

import time
driver = webdriver.Chrome(executable_path="D:\\Selenium\\drivers\\chromedriver.exe")
driver.get("https://www.facebook.com/")
time.sleep(10)
driver.find_element_by_xpath("//*[@id='email']").send_keys("mspsahoo@gmail.com")
driver.find_element_by_xpath('//*[@id="pass"]').send_keys("Nru$!ngha@1946")
driver.find_element_by_xpath('//*[@id="u_0_b"]').click()