from selenium import webdriver
import time
import variables

driver =webdriver.Chrome ("/Users/marysotomayor/Desktop/WebBot2/drivers/chromedriver")


driver.get(variables.shopWebSite)
driver.get(variables.userInterface)

