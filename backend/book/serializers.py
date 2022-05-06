from rest_framework import serializers
from .models import Book


class BookReadSerializer(serializers.ModelSerializer):
    major = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = "__all__"

    def get_major(self, obj):
        return obj.major.name
