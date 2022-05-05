from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Grade, Major


admin.site.register(User, UserAdmin)
admin.site.register(Grade)
admin.site.register(Major)
