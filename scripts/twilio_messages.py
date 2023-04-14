import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

def get_twilio_messages(account_sid, auth_token):
    # Initialize Twilio client
    client = Client(account_sid, auth_token)

    # Retrieve incoming and outgoing messages
    messages = []
    try:
        messages = client.messages.list()
    except TwilioRestException as e:
        print(f"Failed to retrieve messages: {e}")

    return messages

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

print(get_twilio_messages(account_sid, auth_token))
