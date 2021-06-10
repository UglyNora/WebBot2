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
driver.find_element_by_id(variables.startButton).click()

##Compare current date and time to purchase time.
purchaseTime = datetime.datetime(2021,6,10,14,50,00)

while datetime.datetime.now() < purchaseTime :
    time.sleep(1)
    ## Open a new window.
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get(variables.shopWebSite)
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_id(variables.amazonSearchBar).send_keys(variables.mySearch)
driver.find_element_by_id(variables.searchButton).click()
driver.find_element_by_class_name(variables.desiredProduct).click()
buyable = driver.find_element_by_id(variables.buyNowButton)
if buyable.is_displayed():
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element_by_id(variables.yesButton).click()
else:
    driver.find_element_by_id(variables.noButton).click()
