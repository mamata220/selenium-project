from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_driver = webdriver.Chrome(executable_path="D:\\Selenium\\drivers\\chromedriver.exe")

chrome_driver.get("https://www.yatra.com")
print(chrome_driver.title)
chrome_driver.find_element_by_xpath("//*[@id='signInBtn']").click()
time.sleep(20)
email_id = chrome_driver.find_element_by_xpath("//*[@id='login-input']")
if email_id.is_enabled():
    email_id.send_keys("mspsahoo@gmail.com")

chrome_driver.find_element_by_id("login-continue-btn").click()
time.sleep(10)

pwd_field = chrome_driver.find_element_by_xpath("//*[@id='login-password']")
if pwd_field.is_enabled():
    pwd_field.send_keys("Dunu01$220")

login_btn = chrome_driver.find_element_by_id("login-submit-btn")
login_btn.click()

time.sleep(10)
chrome_driver.close()



