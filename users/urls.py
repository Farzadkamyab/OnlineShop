from django.urls import path
from .views import *

app_name = "users"

urlpatterns = [
    path("signup/", UserSignUp.as_view(), name="signUp"),
]