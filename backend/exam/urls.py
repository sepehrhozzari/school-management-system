from rest_framework import routers
from .views import ExamViewSet

router = routers.SimpleRouter()
router.register("exams", ExamViewSet, basename="exams")


app_name = "exam"

urlpatterns = router.urls
