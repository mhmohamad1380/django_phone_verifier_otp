from re import T
import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserOtp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, null=True, blank=False)
    otp = models.CharField(max_length=6, null=True, blank=False)
    uid = models.UUIDField(default=uuid.uuid4,unique=True)

    def __str__(self):
        return f"{self.user} {self.phone_number}"
