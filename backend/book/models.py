from django.db import models
from account.models import Grade, Major


class BookManager(models.Manager):
    def book_count(self):
        return self.count()


class Book(models.Model):
    name = models.CharField(max_length=200, verbose_name="عنوان کتاب")
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE,
                              related_name="books", verbose_name="مقطع تحصیلی کتاب")
    major = models.ForeignKey(Major, on_delete=models.CASCADE,
                              related_name="books", verbose_name="مرتبط به رشته تحصیلی")

    objects = BookManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "کتاب"
        verbose_name_plural = "کتاب ها"
