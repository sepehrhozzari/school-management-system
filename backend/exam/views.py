from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Exam
from .serializers import ExamSerializer
from .permissions import IsTeacherOrReadOnly


class ExamViewSet(ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsTeacherOrReadOnly, ]
    filterset_fields = ["start_date", "time"]
