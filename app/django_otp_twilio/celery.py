import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_otp_twilio.settings")

celery = Celery("django_otp_twilio")
celery.config_from_object("django.conf:settings", namespace="CELERY")
celery.autodiscover_tasks()