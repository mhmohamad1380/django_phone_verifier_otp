from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .mixins import MessageHandler
from main.models import UserOtp
from random import randint
from django.contrib.auth import login, logout
from .tasks import send_message
# Create your views here.

def home_view(request):
    return render(request,"home.html",{})

def register_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == 'POST':
        username = request.POST.get("username")
        phone_number = request.POST.get("phone_number")
        phone_duplicate = UserOtp.objects.filter(phone_number=phone_number)
        user_duplicate = User.objects.filter(username=username)
        if user_duplicate.exists():
            return HttpResponse("This username is not Available!!!")
        if phone_duplicate.exists():
            return HttpResponse("This Phone Number is not Available!!!")
        user = User.objects.create(username=username)
        otp = randint(100000 , 999999)
        user_otp = UserOtp.objects.create(user=user,otp=otp,phone_number=phone_number)

        send_message.delay(phone_number,otp)

        return redirect(f"/verify/{user_otp.uid}")
    return render(request,"register.html",{})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        user_otp = UserOtp.objects.filter(phone_number=phone_number)
        if not user_otp.exists():
            return HttpResponse("this User doesn't exist!!!")
        otp = randint(100000 , 999999)
        user_otp.update(otp=otp)
        send_message.delay(phone_number,otp) 

        return redirect(f"/verify/{user_otp.first().uid}")

    return render(request,"login.html",{})

def verify_otp(request,uid):
    if request.method == "POST":
        otp = request.POST.get("otp")
        user = UserOtp.objects.filter(uid__iexact=uid)
        if not user.exists():
            return HttpResponse("this user doesn't exist!!!")
        else:
            if user.first().otp == otp:
                login(request, user.first().user)
                return redirect("/")
            else:
                return HttpResponse("Code is not Correct!!!")
    return render(request,"otp.html",{})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/")


