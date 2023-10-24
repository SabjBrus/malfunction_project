from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CustomUserViewSet, DepartmentViewSet

router = DefaultRouter()

router.register('users', CustomUserViewSet, basename='users')
router.register('departments', DepartmentViewSet, basename='departments')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
