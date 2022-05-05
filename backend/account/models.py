from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import national_code_validator


class Grade(models.Model):
    name = models.CharField(max_length=10, verbose_name="نام مقطع")

    class Meta:
        verbose_name = "مقطع تحصیلی"
        verbose_name_plural = "مقاطع تحصیلی"

    def __str__(self):
        return self.name


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
    grade = models.ForeIgnKey(Grade, null=True, blank=True, on_delete=models.SET_NULL,
                              related_name="students", verbose_name="مقطع تحصیلی")

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"
        ordering = ("-data_of_birth",)
