from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = [
            'key',
            'created',
            'user_id',
        ]

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 
            'password', 
            'last_login', 
            'is_superuser', 
            'username', 
            'last_name', 
            'email', 
            'is_staff', 
            'is_active', 
            'date_joined', 
            'first_name',
        ]