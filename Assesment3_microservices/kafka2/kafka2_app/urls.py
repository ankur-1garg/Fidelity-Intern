from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'locations', LocationViewSet, basename='location')

# The app_name helps Django identify which app these URLs belong to
app_name = 'kafka2_app'

# URL patterns for our API endpoints
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# Custom admin site settings
admin.site.site_header = 'Kafka2 Location Management'
admin.site.site_title = 'Kafka2 Admin Portal'
admin.site.index_title = 'Welcome to Kafka2 Location Management Portal'
