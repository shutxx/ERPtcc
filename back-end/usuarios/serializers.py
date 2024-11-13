from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.contrib.auth.models import Permission, Group, User


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = [
            'key',
            'created'
        ]

class UsuarioTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 
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

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'codename', 'content_type']

class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']

class UserPermissionSerializer(serializers.ModelSerializer):
    user_permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'user_permissions']