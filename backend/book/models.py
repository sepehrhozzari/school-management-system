from django.db import models
from account.models import Grade, Major


class Book(models.Model):
    name = models.CharField(max_length=200, verbose_name="عنوان کتاب")
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE,
                              related_name="books", verbose_name="مقطع تحصیلی کتاب")
    major = models.ForeignKey(Major, on_delete=models.CASCADE,
                              related_name="books", verbose_name="مرتبط به رشته تحصیلی")

    def __str__(self):
        return self.name
