# importing the requests library
import requests
import time

def execute():

    # api-endpoint
    URL = "http://calls.summitwebsolutions.com/status"

    # sending get request and saving the response as response object
    r = requests.get(url = URL)

    # extracting data in json format
    data = r.json()

    status = data['disarmed']
    return status
