from django.urls import path, include
from rest_framework import routers
from .views import F1DriverViewSet

# Create a router and register our viewset
router = routers.DefaultRouter()
router.register(r'drivers', F1DriverViewSet, basename='f1driver')

# Use the router's URLs
urlpatterns = router.urls
