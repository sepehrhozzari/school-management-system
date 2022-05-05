from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    major = serializers.CharField(source="major.name")
    grade = serializers.CharField(source="grade.name")

    class Meta:
        model = User
        exclude = ("password", "user_permissions", "groups")
