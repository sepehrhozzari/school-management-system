from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "major", "grade")
    list_filter = ("major", "grade")
    search_fields = ("name",)


admin.site.register(Book, BookAdmin)
