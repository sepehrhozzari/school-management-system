from django.db import models
from account.models import Grade


class Book(models.Model):
    name = models.CharField(max_length=200, verbose_name="عنوان کتاب")
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE,
                              related_name="books", verbose_name="مقطع تحصیلی کتاب")
