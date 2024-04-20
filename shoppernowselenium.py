from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import pandas as pd

driver = webdriver.Chrome()
#driver.get('https://www.google.com')

driver.get('https://www.shoppernow.com.au/Account/Login.aspx')

USERNAME = "***REMOVED***"
PASSWORD = "***REMOVED***"

# what is with these variable names im gonna be sick
login = driver.find_element("xpath","//input[@name='ctl00$MainContent$Email']").send_keys(USERNAME)
password = driver.find_element("xpath","//input[@name='ctl00$MainContent$Password']").send_keys(PASSWORD)
submit = driver.find_element("xpath","//input[@type='submit']").click()

# for some cursed reason you have to log in twice
login = driver.find_element("xpath","//input[@name='ctl00$MainContent$Email']").send_keys(USERNAME)
password = driver.find_element("xpath","//input[@name='ctl00$MainContent$Password']").send_keys(PASSWORD)
submit = driver.find_element("xpath","//input[@type='submit']").click()


wait = WebDriverWait(driver, 30).until(
        lambda driver: driver.current_url != "https://www.shoppernow.com.au/Account/Login.aspx")


jobBoard = driver.find_element(By.ID,"MainContent_lnkJobBoard").click()
wait = WebDriverWait(driver, 30).until(
        lambda driver: driver.current_url != "https://www.shoppernow.com.au/Dashboard/Dashboard")



try:
    logout_button =  driver.find_element("xpath","//a[@href='javascript:__doPostBack('ctl00$header$ctl00$ctl02$ctl00','')']").click()
    print('Successfully logged in')
except:
    print('Incorrect login/password')
