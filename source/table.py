from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\\Selenium\\drivers\\chromedriver.exe")
#driver.get("http://localhost:63342/selenium%20project/source/tableforcode.html?_ijt=k12ms3j8vsjcrii0oo1u7gqncb")
driver.get("file:///C:/Users/shiba/PycharmProjects/selenium%20project/source/tableforcode.html")

rows = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))
cols = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th"))

print("Size of rows: " + str(rows))
print("Siz of cols: " + str(cols))
print()
print("Firstname"+"   "+"Lastname"+"   "+"age")

for r in range(2, rows + 1):
    for c in range(1, cols+1):
        value = driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value, end=" ")
        print()




       # print()



