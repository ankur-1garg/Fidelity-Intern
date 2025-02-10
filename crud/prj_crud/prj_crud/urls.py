"""
URL configuration for prj_crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from crud_app import views  # Corrected import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', views.orders, name='orders'),
    path('showorders/', views.showorders, name='showorders'),
    path('updateord/<int:id>/', views.updateord, name='updateord'),
    path('deleteord/<int:id>/', views.deleteord, name='deleteord'),
    path('setsession/', views.setsession, name='setsession'),
    path('getsession/', views.getsession, name='getsession'),
]
