def execute():

    # importing the requests library
    import requests

    # defining the api-endpoint
    API_ENDPOINT = "http://calls.summitwebsolutions.com/arm"

    # your API key here
    API_KEY = "XXXXXXXXXXXXXXXXX"

    # data to be sent to api
    data = {'disarmed':0}

    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, data = data)

    # extracting response text
    #pastebin_url = r.text
    #print("The pastebin URL is:%s"%pastebin_url)
