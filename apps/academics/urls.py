from django.urls import path
from .views import (
    SubjectAPIView,
    SchoolClassAPIView,
    TeacherProfileAPIView,
    StudentProfileAPIView,
)

urlpatterns = [
    path("subjects/", SubjectAPIView.as_view(), name="subjects"),
    path("classes/", SchoolClassAPIView.as_view(), name="classes"),
    path("teachers/", TeacherProfileAPIView.as_view(), name="teachers"),
    path("students/", StudentProfileAPIView.as_view(), name="students"),
]
