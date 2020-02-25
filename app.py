from twilio.rest import Client
from vars import TWILIO_ACCOUNT_SID, TWILIO_NUMBER, TWILIO_AUTH_TOKEN
from vars import SIP_NUMBER
from vars import RECIPIENTS

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


for i in RECIPIENTS:    

    message = client.messages.create(
#        body='Please call this number now: ' + SIP_NUMBER, 
        body='Test message from Sham - please ignore!',
        from_=TWILIO_NUMBER,
        to=i
    )

