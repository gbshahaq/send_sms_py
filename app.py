from twilio.rest import Client
from vars import TWILIO_ACCOUNT_SID, TWILIO_NUMBER, TWILIO_AUTH_TOKEN
from vars import SIP_NUMBER
from body import BODY
#from recipients import RECIPIENTS

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

recipients = open("recip_list.txt","r")

for l in recipients:
#for i in RECIPIENTS:    

    message = client.messages.create(
        body=BODY + SIP_NUMBER, 
#        body='Test message from xxx - please ignore!',
        from_=TWILIO_NUMBER,
        to=l
    )

recipients.close()

