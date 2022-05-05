from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Grade, Major

UserAdmin.list_display += ("is_student", "is_teacher",
                           "grade", "major", "father_name")

admin.site.register(User, UserAdmin)
admin.site.register(Grade)
admin.site.register(Major)
