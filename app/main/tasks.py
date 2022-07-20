from celery import shared_task
from .mixins import MessageHandler

@shared_task
def send_message(phone_number,otp):
    MessageHandler(phone_number,otp).send_otp_to_the_phone()