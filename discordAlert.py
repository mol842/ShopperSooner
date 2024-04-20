import os
import requests

DISCORD_WEBHOOK_URL = "***REMOVED***W"


def sendDiscordAlert(messageStr):
    payload = {'content': messageStr}
    response = requests.post(DISCORD_WEBHOOK_URL, json=payload)

def formatJobAlert(jobTuplesList):
    message = "Alert! I found some jobs you may be interested in:\n"
    for job in jobTuplesList:
        message += "[{}](https://www.shoppernow.com.au/Shopper/JobDetail.aspx?JobID={})".format(job[0], job[1])
        message += " - {}".format(job[2])
        message += "\n"
    message += "Have a good day!!"
    return message