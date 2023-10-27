from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from defects.models import Defect
from users.models import CustomUser, Department


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'password')


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'slug', 'email')


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'slug')


class DefectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defect
        fields = (
            'id',
            'title',
            'body',
            'priority',
            'status',
            'created_at',
            'department',
        )
