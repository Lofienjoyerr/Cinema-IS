from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "phone", "is_active", "is_staff", "is_superuser"]

    def to_representation(self, instance: User):
        return {
            "id": instance.id,
            "username": instance.username,
            "password": instance.password,
            "email": instance.email,
            "phone": instance.phone,
            "is_active": instance.is_active,
            "is_staff": instance.is_staff,
            "is_superuser": instance.is_superuser,
        }
