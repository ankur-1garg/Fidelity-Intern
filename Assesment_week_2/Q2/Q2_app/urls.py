from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Q2_app.views import QuestionPaperViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Create router and register viewset
router = DefaultRouter()
router.register('questions', QuestionPaperViewSet, basename='question')

# Swagger schema configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Question Paper API",
        default_version='v1',
        description="API for managing question papers",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
