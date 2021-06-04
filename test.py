from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
import variables

driver = webdriver.Chrome ("/Users/marysotomayor/Desktop/WebBot2/drivers/chromedriver")


## Opens a user interface.
driver.get(variables.userInterface)
driver.maximize_window()
driver.implicitly_wait(10)

## Select a specific date and time.
driver.find_element_by_id("purchasetime").send_keys(variables.myDate)
driver.find_element_by_id("purchasetime").send_keys(Keys.TAB)
driver.find_element_by_id("purchasetime").send_keys(variables.myTime)

## Submit form.
driver.find_element_by_id("submitbutton").click()

## Begin countdown to purchase time.
driver.find_element_by_id("start").click()

## Wait until expected date reached to purchase desired item.
target_time = datetime.datetime(2021, 6, 4, 9, 59, 0)  
while not (target_time == datetime.datetime.now()) :
    print(datetime.datetime.now() )
    time.sleep()
    if target_time == datetime.datetime.now():
        driver.get(variables.shopWebSite)
        driver.maximize_window()
        driver.implicitly_wait(10)

