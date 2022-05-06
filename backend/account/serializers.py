from rest_framework import serializers
from .models import User, Grade, Major


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = "__all__"


class UserReadSerializer(serializers.ModelSerializer):
    major = MajorSerializer()
    grade = GradeSerializer()

    class Meta:
        model = User
        exclude = ("user_permissions", "groups")


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("user_permissions", "groups")

    def validate_national_code(self, value):
        if value == "":
            return value
        else:
            if User.objects.filter(national_code=value).exists():
                raise serializers.ValidationError(
                    "این کد ملی قبلا برای یک کاربری دیگر است")
            else:
                return value
