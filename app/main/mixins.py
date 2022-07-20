from twilio.rest import Client
from django.conf import settings

class MessageHandler:
    phone_number = None
    otp = None

    def __init__(self, phone_number, otp):
        self.phone_number = phone_number
        self.otp = otp

    def send_otp_to_the_phone(self):
        client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)

        message = client.messages.create(
            body=f"Your OTP Code is: {self.otp}",
            from_="+18646642071",
            to=self.phone_number,
        )