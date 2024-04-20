import time
from shopperNowScraper import scrapeNewJobs

# added Northland just for testing, modify as needed
DISPLAYUI = False
MAXCYCLES = 100
SLEEPTIME = 1000 # 3 mins idk

KEYWORDS = ["Woolworths", "Dan", "Murphys", "Online", "Uber", "UberVCExpress", "Delivery", "Northland"]
USERNAME = "***REMOVED***"
PASSWORD = "***REMOVED***"


i = 0
while i < MAXCYCLES:
   scrapeNewJobs(DISPLAYUI, KEYWORDS, USERNAME, PASSWORD)
   i+=1
   print("Cycle: " + str(i))
   time.sleep(SLEEPTIME)
