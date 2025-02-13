from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.inventory_list, name='inventory-list'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='registration/logged_out.html',
        next_page='login'
    ), name='logout'),
    path('inventory/<int:pk>/', views.inventory_detail, name='inventory-detail'),
    path('inventory/new/', views.inventory_create, name='inventory-create'),
    path('inventory/<int:pk>/edit/',
         views.inventory_update, name='inventory-update'),
    path('inventory/<int:pk>/delete/',
         views.inventory_delete, name='inventory-delete'),
]
