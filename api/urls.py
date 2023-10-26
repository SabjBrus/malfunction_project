from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CustomUserViewSet, DepartmentViewSet, DefectViewSet

router = DefaultRouter()

router.register('users', CustomUserViewSet, basename='users')
router.register('departments', DepartmentViewSet, basename='departments')
router.register('defects', DefectViewSet, basename='defects')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
