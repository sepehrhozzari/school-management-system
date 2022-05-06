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


class UserSerializer(serializers.ModelSerializer):
    major = MajorSerializer()
    grade = GradeSerializer()

    class Meta:
        model = User
        exclude = ("user_permissions", "groups")

    def create(self, validated_data):
        # pop grade name and major name from validated_data
        grade_data = validated_data.pop("grade")
        major_data = validated_data.pop("major")

        # get grade and major instacne
        try:
            major = Major.objects.get(**major_data)
        except:
            raise serializers.ValidationError(
                "رشته ای که مورد نظر آن بوده اید پیدا نشده است")
        try:
            grade = Grade.objects.get(**grade_data)
        except:
            raise serializers.ValidationError(
                "مقطع تحصیلی که مورد نظر آن بوده اید پیدا نشده است")

        # create user
        user = User.objects.create(**validated_data, grade=grade, major=major)
        return user

    def update(self, instance, validated_data):
        # get grade name and major name from validated_data
        major_data = validated_data.get("major", "")
        grade_data = validated_data.get("grade", "")

        # get grade and major instacne
        try:
            major = Major.objects.get(**major_data)
        except:
            raise serializers.ValidationError(
                "رشته ای که مورد نظر آن بوده اید پیدا نشده است")
        try:
            grade = Grade.objects.get(**grade_data)
        except:
            raise serializers.ValidationError(
                "مقطع تحصیلی که مورد نظر آن بوده اید پیدا نشده است")

        # update user
        validated_data["major"] = major
        validated_data["grade"] = grade
        return super().update(instance, validated_data)
