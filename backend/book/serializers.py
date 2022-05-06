from rest_framework import serializers
from .models import Book


class BookReadSerializer(serializers.ModelSerializer):
    major = serializers.SerializerMethodField()
    grade = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = "__all__"

    def get_major(self, obj):
        return obj.major.name

    def get_grade(self, obj):
        return obj.grade.name


class BookPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
