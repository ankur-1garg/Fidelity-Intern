from django.contrib import admin
from django.urls import path, include  # Importing path and include for URL routing

# URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # URL pattern for the admin site
    path('', include('inventory.urls')),  # Including URL patterns from the inventory app
]