import os
from twilio.rest import Client
from twilio.twiml.voice_response import Gather, VoiceResponse

def execute():

    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = 'AC37f2606a24c4ad673886172e74eee4fe'
    #account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = '12fb4fc8499498c02403a01c0ff044f8'
    #auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)


    call = client.calls.create(
                            url='http://calls.summitwebsolutions.com/arm',
                            to='+12673570079',
                            from_='+19804304246',
                        )

    print(call.sid)
