from django.urls import path
from .views import *


urlpatterns = [
    path("products/<int:pk>", ProductView.as_view(), name="products"),
    path("search-result", SearchProductView.as_view(), name="search"),
]