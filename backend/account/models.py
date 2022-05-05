from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import national_code_validator


class User(AbstractUser):
    is_student = models.BooleanField(default=False, verbose_name="دانش آموز")
    is_teacher = models.BooleanField(default=False, verbose_name="معلم")
    national_code = models.CharField(max_length=10, unique=True, validators=[
                                     national_code_validator])
    profile_picture = models.ImageField(upload_to="account/")
    address = models.TextField(verbose_name="آدرس")
    data_of_birth = models.DateTimeField(
        verbose_name="تاریخ تولد", null=True, blank=True)
    father_name = models.CharField(
        max_length=200, null=True, blank=True, verbose_name="نام پدر")
