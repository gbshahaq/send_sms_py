from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import phonenumbers

from vars import TWILIO_ACCOUNT_SID, TWILIO_NUMBER, TWILIO_AUTH_TOKEN
from vars import SIP_NUMBER
from body import BODY
#from recipients import RECIPIENTS

# establish Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

#open file for reading
recipients = open("recip_list.txt","r")

#loop through entries of phone numbers
for line in recipients:
        try:
            message = client.messages.create(
                body=BODY + SIP_NUMBER, 
                from_=TWILIO_NUMBER,
                to=line
                )
        except TwilioRestException:
            print("Twilio REST error with number " + line)

recipients.close()

