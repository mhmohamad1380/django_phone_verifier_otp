from django.urls import path
from .views import *

urlpatterns = [
    path("register", register_view),
    path("", home_view),
    path("verify/<uid>",verify_otp),
    path("logout",logout_view),
    path("login",login_view)

]