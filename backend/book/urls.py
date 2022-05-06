from rest_framework import routers
from .views import BookViewSet


router = routers.SimpleRouter()
router.register("books", BookViewSet, basename="books")


app_name = "book"

urlpatterns = router.urls
