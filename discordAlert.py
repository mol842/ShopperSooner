import requests
import config

# import from config file
# DISCORD_WEBHOOK_URL = "***REMOVED***" 


def sendDiscordAlert(messageStr):
    payload = {'content': messageStr}
    response = requests.post(config.DISCORD_WEBHOOK_URL, json=payload)

def formatJobAlert(jobTuplesList):
    message = "Alert! I found some jobs you may be interested in:\n"
    for job in jobTuplesList:
        message += "[{}](https://www.shoppernow.com.au/Shopper/JobDetail.aspx?JobID={})".format(job[0], job[1])
        message += " - {}".format(job[2])
        message += "\n"
    return message