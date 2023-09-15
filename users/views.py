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

