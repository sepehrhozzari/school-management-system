from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAdminUser
from .permissions import IsAdminOrStudent, IsSuperUser


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAdminUser, ]
        elif self.action == "create":
            permission_classes = [IsSuperUser, ]
        else:
            permission_classes = [IsAdminOrStudent, ]
        return [permission() for permission in permission_classes]
