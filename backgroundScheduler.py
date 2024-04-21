import time
from shopperNowScraper import scrapeNewJobs
import config

# added Northland just for testing, modify as needed
DISPLAYUI = False
MAXCYCLES = 100
SLEEPTIME = 1000 # 3 mins idk

KEYWORDS = ["Woolworths", "Dan", "Murphys", "Online", "Uber", "UberVCExpress", "Delivery", "Northland"]

## import from config file
#USERNAME = "***REMOVED***"
#PASSWORD = "***REMOVED***"


i = 0
while i < MAXCYCLES:
   scrapeNewJobs(DISPLAYUI, KEYWORDS, config.USERNAME, config.PASSWORD)
   i+=1
   print("Cycle: " + str(i))
   time.sleep(SLEEPTIME)
