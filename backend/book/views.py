from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookReadSerializer, BookPostSerializer
from account.permissions import IsAdminOrTeacher


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [IsAdminOrTeacher, ]
    filterset_fields = ("major", "grade")
    search_fields = ("name",)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return BookReadSerializer
        else:
            return BookPostSerializer
