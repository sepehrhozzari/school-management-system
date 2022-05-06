from django.db import models


class Exam(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان امتحان")
    description = models.TextField(verbose_name="توضیحات امتحان")
    start_date = models.DateTimeField(verbose_name="زمان شروع امتحان")
    time = models.IntegerField(verbose_name="مدت زمان(به دقیقه)")

    def __str__(self):
        return self.title
