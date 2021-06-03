from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import variables

driver = webdriver.Chrome ("/Users/marysotomayor/Desktop/WebBot2/drivers/chromedriver")


#Opens a user interface.
driver.get(variables.userInterface)
driver.maximize_window()
driver.implicitly_wait(10)

## Select a specific date and time.
driver.find_element_by_id("purchasetime").send_keys(variables.myDate)
driver.find_element_by_id("purchasetime").send_keys(Keys.TAB)
driver.find_element_by_id("purchasetime").send_keys(variables.myTime)


driver.find_element_by_id("submitbutton").click()
