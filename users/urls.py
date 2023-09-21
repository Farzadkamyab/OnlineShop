from django.urls import path
from .views import *

app_name = "users"

urlpatterns = [
    path("signup/", UserSignUp.as_view(), name="signUp"),
    path("login/", UserLogin.as_view(), name="login"),
    path("otp-check/", CheckOtp.as_view(), name="otp"),
    path("logout/", UserLogout.as_view(), name="logout"),
]