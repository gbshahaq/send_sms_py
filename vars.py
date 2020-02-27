!#/usr/bin/python3
# get env variables
import os

# set identifiers as local environment variables
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', None)
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', None)
TWILIO_NUMBER = os.environ.get('TWILIO_MOBILE', None)

SIP_NUMBER = os.environ.get('TWILIO_SIP_NUMBER', None)


