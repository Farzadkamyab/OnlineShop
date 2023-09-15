from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager
from .validation import phone_number_validator
from django.core.exceptions import ValidationError
import re

class PhoneNumberField(models.CharField):
    def get_prep_value(self, value):
        if value is None:
            return value

        try:
            regex = phone_number_validator(value)
        except ValidationError:
            raise ValidationError(
                "Phone number must be entered in the format: '09XXXXXXXXX', '00989XXXXXXXXX' or '+989XXXXXXXXX'."
            )

        formatted_phone_number = re.sub(r"^\+98|^0098", "0", value)
        return formatted_phone_number



# Create your models here.
