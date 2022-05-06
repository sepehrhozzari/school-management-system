from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet

app_name = "account"


router = routers.SimpleRouter()
router.register(r"users", UserViewSet, basename="users")


urlpatterns = router.urls
