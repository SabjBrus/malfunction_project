from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from api.views import CustomUserViewSet, DefectViewSet, DepartmentViewSet

schema_view = get_schema_view(
    openapi.Info(
        title='Malfunction API',
        default_version='v1',
        description='Документация для проекта Malfunction',
        contact=openapi.Contact(email='admin@malfunction_project.ru'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()

router.register('users', CustomUserViewSet, basename='users')
router.register('departments', DepartmentViewSet, basename='departments')
router.register('defects', DefectViewSet, basename='defects')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
]
