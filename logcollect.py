
from twilio.rest import Client
from vars import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, SIP_NUMBER


client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# log who called and put them in the list to be messaged
calls = client.calls.list(status="completed", page_size = "200", start_time_after="2020-03-10 08:00:00")

#recipients = open("recip_list.txt","a")
print("SID" + " " + "TO" + " " + "FROM" + " " + "DUR" + " " + "TIMESTAMP")
for record in calls:
       #   if(record.from_[0:3])=="+91": 
                tm = record.end_time
                rec = record.sid + " " + record.to + " " + record.from_ + " " + record.duration + " " + format(tm)
                print(rec)
                #recipients.write(rec + "/r")
# print(record.from_)
# recipients.write(record.sid + " " + record.duration + " " + record.status + "\r")

# recipients.close()
