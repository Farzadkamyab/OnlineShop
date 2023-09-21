from django.urls import path
from .views import *


urlpatterns = [
    path("products/<int:pk>", ProductView.as_view(), name="products"),
]