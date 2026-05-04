from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User
from rest_framework import serializers


# transformation logic
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user

        data["user"] = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": getattr(user, "role", None),
        }

        return data


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "role"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            role=validated_data.get("role", "STUDENT"),
        )
        return user
