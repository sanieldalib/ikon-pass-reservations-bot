import os
from twilio.rest import Client

from config import PHONES

class TwilioSms:
    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ['TWILIO_TOKEN'])
        self.phone = os.environ['TWILIO_PHONE']
    
    def send_message(self, message, phone):
        self.client.messages.create(
                     body=message,
                     from_=self.phone,
                     to=phone
                 )

    def notify_preferences(self, preferences):
        all_false = True
        for pref in preferences:
            if pref.available:
                all_false = False
                for phone in PHONES:
                    print(pref.sms_text())
                    self.send_message(pref.sms_text(), phone)
        # if all_false:
        #     for phone in PHONES:
        #         self.send_message('No new reservations.', phone)