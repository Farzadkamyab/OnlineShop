import random
import re
from .models import CustomUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSignUpSerializer, UserLoginSerializer, UserAddressSerializer, OtpSerializer
from rest_framework import status
from .authentication import CustomAuthBackend
from django.contrib.auth import login, logout

# Create your views here.
class UserSignUp(APIView):
    def post(self, request):
        srz_data = UserSignUpSerializer(request.POST)
        address_srz = UserAddressSerializer(request.POST)

        if srz_data.is_valid():
            srz_data.save()
            if address_srz.is_valid():
                address_srz.save()
                context = {
                    "user_info": srz_data.data,
                    "user_address": address_srz.data
                }
                return Response(context, status=status.HTTP_200_OK)
        else:
            return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    def post(self, request):
        srz_data = UserLoginSerializer(request.POST)
        if srz_data.is_valid():
            random_code = random.randint(1000, 9999)
            print(f"Your OTP: {random_code}")
            CustomUser.objects.update(code=random_code)
            phone_number = srz_data.validated_data.get("phone_number")
            formatted_phone_number = re.sub(r"^\+98|^0098", "0", phone_number)

            user = CustomUser.objects.filter(phone_number=formatted_phone_number).first()

            if user is None:
                return Response({"message": "User not found."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                # send_OTP(formatted_phone_number, random_code)
                request.session["user_info"] = {"phone_number": formatted_phone_number, "code": random_code}

                return Response({"message": "Otp code has send successfully..."}, status=status.HTTP_200_OK)

class CheckOtp(APIView):
    def post(self, request):
        srz_data = OtpSerializer(request.POST)
        if srz_data.is_valid():
            otp = srz_data.validated_data["code"]
            user = CustomAuthBackend.authenticate(request,phone_number=request.session["user_info"]["phone_number"],code=otp)
            if user is not None:
                login(request, user, backend="django.contrib.auth.backends.ModelBackend")
                return Response({'message': "you are logged in successfully."}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Entered wrong password."}, status=status.HTTP_400_BAD_REQUEST)

class UserLogout(APIView):
    def get(self, request):
        logout(request)
        return Response({'message': "you are logged out successfully."}, status=status.HTTP_200_OK)