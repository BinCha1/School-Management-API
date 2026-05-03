from django.urls import path
from .views import CustomTokenObtainPairView, ProfileView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    path(
        "me/", ProfileView.as_view(), name="profile"
    ),  # “Give me the currently logged-in user’s profile using the JWT access token.”
]
