from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from phonenumbers import parse, phonenumberutil
from vars import TWILIO_ACCOUNT_SID, TWILIO_NUMBER, TWILIO_AUTH_TOKEN, TWILIO_MSG_SVC
from vars import SIP_NUMBER
from body import BODY

# establish Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

#open file for reading
recipients = open("recip_list.txt","r")

#loop through entries of phone numbers
# nested try/except - test for parse and twilio exceptions
for line in recipients:
        try:
            x = parse(line, None)
            try:
                message = client.messages.create(
                    body=BODY, 
#                    from_=TWILIO_NUMBER,
                    messaging_service_sid=TWILIO_MSG_SVC,
                    to=line
                    )
            except TwilioRestException:
                print("Twilio REST error with number " + line)
        except phonenumberutil.NumberParseException:
            print(line + " does not look like a phone number in E.164 format")      

recipients.close()

