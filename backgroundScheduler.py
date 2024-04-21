import time
from shopperNowScraper import scrapeNewJobs
import config
import pickle


# added Northland just for testing, modify as needed
DISPLAYUI = True
MAXCYCLES = 100
SLEEPTIME = 1000 # 3 mins idk

KEYWORDS = ["Woolworths", "Dan", "Murphys", "Online", "Uber", "UberVCExpress", "Delivery", "Optus", "BWS"]
LOGFILE = "log.pk"


## import from config file
#USERNAME = "***REMOVED***"
#PASSWORD = "***REMOVED***"

sentJobs = []

i = 0
while i < MAXCYCLES:
   sentJobs = scrapeNewJobs(DISPLAYUI, KEYWORDS, config.USERNAME, config.PASSWORD, sentJobs)

   i+=1
   print("Cycle: " + str(i))

   with open(LOGFILE, 'wb') as fi:
      pickle.dump(sentJobs, fi)

   time.sleep(SLEEPTIME)
