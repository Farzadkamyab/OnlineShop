from rest_framework import serializers
from .models import CustomUser, Address

class UserSignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ["phone_number", "password", "password2", "first_name", "last_name"]

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["phone_number", "password"]
    
class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class OtpSerializer(serializers.Serializer):
    otp = serializers.IntegerField()

class UserCompleteInfo(serializers.Serializer):
    user_info = UserSignUpSerializer()
    user_address = UserAddressSerializer()

    def create(self, validated_data):
        return super().create(validated_data)