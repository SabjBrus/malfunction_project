from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from api.serializers import CustomUserSerializer, DepartmentSerializer, DefectSerializer
from defects.models import Defect
from api.pagination import DefectsPagination
from api.permissions import OwnerOrReadOnly
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
    permission_classes = (OwnerOrReadOnly,)
    pagination_class = DefectsPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('priority', 'status')
