from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

User = get_user_model()


class UserSerializer(ModelSerializer):
    user = None

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'country']

    def create(self, validated_data):
        self.user = User.objects.create_user(**validated_data)
        return self.user


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['email', 'password']