from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('users', CustomUserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
