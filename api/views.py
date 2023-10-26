from rest_framework import viewsets

from api.serializers import CustomUserSerializer, DepartmentSerializer, DefectSerializer
from defects.models import Defect
from users.models import CustomUser, Department


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DefectViewSet(viewsets.ModelViewSet):
    queryset = Defect.objects.all()
    serializer_class = DefectSerializer
