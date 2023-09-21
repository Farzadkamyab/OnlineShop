from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = "__all__"

class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = "__all__"
