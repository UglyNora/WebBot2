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
driver.find_element_by_id(variables.purchaseTime).send_keys(variables.myDate)
driver.find_element_by_id(variables.purchaseTime).send_keys(Keys.TAB)
driver.find_element_by_id(variables.purchaseTime).send_keys(variables.myTime)

## Submit form.
driver.find_element_by_id(variables.submitButton).click()

## Begin countdown to purchase time.
driver.find_element_by_id(startButton).click()

## Wait until expected date reached to purchase desired item.
date = variables.expectedDate
targetTime = ''.join([i for i in date if i.isdigit()])
print(targetTime)
while not (targetTime == datetime.datetime.now()) :
    time.sleep(10)
    if targetTime == datetime.datetime.now():
        driver.get(variables.shopWebSite)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element_by_id(variables.amazonSearchBar).send_keys(variables.mySearch)
        driver.find_element_by_id(variables.searchButton).click()
        driver.find_element_by_xpath(variables.desiredProduct).click()
        driver.find_element_by_id(variables.buyNowButton).click()