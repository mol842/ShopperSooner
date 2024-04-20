from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from discordAlert import sendDiscordAlert, formatJobAlert


def scrapeNewJobs(displayUI, keywords, username, password):
    chrome_options = Options()
    if not displayUI:
        chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(chrome_options)
    driver.get('https://www.shoppernow.com.au/Account/Login.aspx')

    # what is with these variable names im gonna be sick
    login = driver.find_element("xpath","//input[@name='ctl00$MainContent$Email']").send_keys(username)
    passwordd = driver.find_element("xpath","//input[@name='ctl00$MainContent$Password']").send_keys(password)
    submit = driver.find_element("xpath","//input[@type='submit']").click()

    # for some cursed reason you have to log in twice
    login = driver.find_element("xpath","//input[@name='ctl00$MainContent$Email']").send_keys(username)
    passwordd = driver.find_element("xpath","//input[@name='ctl00$MainContent$Password']").send_keys(password)
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

    importantJobs = []
    for job in jobInfo:
        print(job)
        if any(word in job[0] for word in keywords):
            importantJobs.append(job)

    if len(importantJobs) > 0:
        alert = formatJobAlert(importantJobs)
        sendDiscordAlert(alert)

    print("done")



