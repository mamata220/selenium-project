from selenium import webdriver
chrome_driver = webdriver.Chrome(executable_path="D:\\Selenium\\drivers\\chromedriver.exe")
chrome_driver.maximize_window()

chrome_driver.implicitly_wait(20)
assert "Expedia Travel: Search Hotels, Cheap Flights, Car Rentals & Vacations" in chrome_driver.title
chrome_driver.get('https://www.expedia.com/')
