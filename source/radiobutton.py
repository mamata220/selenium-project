from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

chrome_driver = webdriver.Chrome(executable_path="D:\\Selenium\\drivers\\chromedriver.exe")

chrome_driver.get("https://www.iciciprulife.com/")
chrome_driver.maximize_window()
time.sleep(10)

if chrome_driver.find_element_by_id("login-toggle").is_displayed():
    chrome_driver.find_element_by_id("login-toggle").click()

time.sleep(5)
if chrome_driver.find_element_by_id("login-type").is_displayed():
    drp = Select(chrome_driver.find_element_by_id("login-type"))
    print(len(drp.options))
    all_options = drp.options
    for options in all_options:
        print(options.text)

time.sleep(20)

drp1 = Select(chrome_driver.find_element_by_class_name("ipru-nav-text"))
print(len(drp1.options))
all_options = drp1.options
for options in all_options:
    print(options.text)

chrome_driver.close()
