from django.contrib import admin
from .models import Exam


class ExamAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "start_date", "time")
    list_filter = ("start_date",)
    ordering = ("-start_date",)


admin.site.register(Exam, ExamAdmin)
