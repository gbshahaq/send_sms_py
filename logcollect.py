
from twilio.rest import Client
from vars import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, SIP_NUMBER

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# log who called and put them in the list to be messaged
calls = client.calls.list(status="completed", page_size = "200", start_time_after="2020-03-04 16:00:00")
recipients = open("recip_list.txt","w")

for record in calls:
     if(record.to[0:3])=="sip": 
        # tm = record.end_time
        # print(record.to + ":" + record.from_ + " " + record.duration + " " + format(tm))
        # print(record.from_)
        recipients.write(record.from_ + "\r")

recipients.close()
