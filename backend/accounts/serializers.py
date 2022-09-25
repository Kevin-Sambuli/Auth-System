from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from .models import Account

from djoser.serializers import UserCreateSerializer

User = get_user_model()


# class AccountSerializer(ModelSerializer):
#     class Meta:
#         model = Account
#         fields = []

class AccountSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'username']
