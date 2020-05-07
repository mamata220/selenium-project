from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="D:\\Selenium\\drivers\\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
links = driver.find_elements_by_tag_name("a")
print(len(links))
for link in links:
    print(link.text, end="  :  " + link.get_attribute("href"))
    print()







