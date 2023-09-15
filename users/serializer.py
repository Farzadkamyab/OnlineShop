from rest_framework import serializers
from .models import CustomUser, Address

class UserSignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ["phone_number", "password", "password2", "first_name", "last_name"]

