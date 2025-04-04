from rest_framework import permissions, routers

from django.contrib import admin
#from django.conf.urls import url
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from cats.views import AchievementViewSet, CatViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'users', UserViewSet)
router.register(r'achievements', AchievementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]


schema_view = get_schema_view(
    openapi.Info(
        title="Cats API",
        default_version="v1",
        description="Documentation for cats app of Kittygram project",
        contact=openapi.Contact(email="admin@kittygram.ru"),
        license=openapi.License(name="BSD license"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns += [
    path(
        'swagger<format>/',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]
