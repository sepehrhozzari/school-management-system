from django.core.exceptions import ValidationError


def national_code_validator(value):
    if value == str:
        raise ValidationError("کد ملی باید عدد باشد")
    return value
