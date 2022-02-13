from django.core.exceptions import ValidationError
import re

phone_pattern = r"^(09)([0-9]{9})$"


def validate_phone(phone):
    if not re.match(phone_pattern, phone):
        raise Exception('number should be 11 and numeric')


def validate_password(password):
    if not (len(password) >= 8):
        raise Exception('password should be more than 8 character')

