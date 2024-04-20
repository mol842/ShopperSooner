from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from discordAlert import sendDiscordAlert, formatJobAlert

KEYWORDS = ["Woolworths", "Dan", "Murphys", "Online", "Uber", "UberVCExpress", "Delivery", "Northland"]

driver = webdriver.Chrome()
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


# navigate to da job board
jobBoard = driver.find_element(By.ID,"MainContent_lnkJobBoard").click()

wait = WebDriverWait(driver, 30).until(
        lambda driver: driver.current_url != "https://www.shoppernow.com.au/Dashboard/Dashboard")

# get a list of all jobs avaliable
jobs = driver.find_elements("xpath", "//*[contains(@id,'lblJobName')]")
ids = driver.find_elements("xpath", "//*[contains(@id,'lblJobId')]")
departments = driver.find_elements("xpath", "//*[contains(@id,'lblDepartment')]")


jobNames = [job.text for job in jobs]
idStrs = [id.text for id in ids]
deptNames = [dept.text for dept in departments]

# put into a tuple. assumes all jobs have all 3 provided
# yeah no error handling here we live on the edge
jobInfo = zip(jobNames, idStrs, deptNames)

print(jobInfo)

importantJobs = []
for job in jobInfo:
    if any(word in job[0] for word in KEYWORDS):
        importantJobs.append(job)
    print(job)

if len(importantJobs) > 0:
    print("iimportsnt")
    alert = formatJobAlert(importantJobs)
    sendDiscordAlert(alert)

print("done")



