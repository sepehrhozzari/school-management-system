from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Grade, Major

UserAdmin.fieldsets[2][1]["fields"] += ("is_teacher", "is_student")
UserAdmin.fieldsets += ("اطلاعات عمومی", {"fields": ("national_code", "profile_picture",
                        "address", "data_of_birth", "father_name", "grade", "major")}),

UserAdmin.list_display += ("is_student", "is_teacher",
                           "grade", "major", "father_name")
UserAdmin.list_filter += ("is_teacher", "is_student",
                          "data_of_birth", "major", "grade")
UserAdmin.search_fields += ("national_code", "father_name")

admin.site.register(User, UserAdmin)
admin.site.register(Grade)
admin.site.register(Major)
