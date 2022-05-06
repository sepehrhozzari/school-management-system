from django.contrib import admin
from .models import Exam


class ExamAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "start_date", "time")


admin.site.register(Exam, ExamAdmin)
