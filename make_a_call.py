import os
import time
from twilio.rest import Client
from twilio.twiml.voice_response import Gather, VoiceResponse

def execute():

    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)


    call = client.calls.create(
                            url='http://calls.summitwebsolutions.com/arm',
                            to='+12673570079',
                            from_='+19804304246',
                        )

    #check_the_alarm.execute()
