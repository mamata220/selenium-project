from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://letskodeit.teachable.com/p/practice")
time.sleep(5)

multi_select = driver.find_element_by_id("multiple-select-example")
#driver.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div[1]/div[3]/fieldset/select/option[2]")
if driver.find_element_by_id("multiple-select-example").is_displayed():
    drp = Select(driver.find_element_by_id("multiple-select-example"))

    time.sleep(5)
    #drp.select_by_visible_text("Peach")
    all_sel_options = drp.all_selected_options
    print("User selected counts: ", len(all_sel_options), " Below are the chosen values: ")
    for sel_option in all_sel_options:
        print(sel_option.text)



