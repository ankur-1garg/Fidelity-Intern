from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # URL pattern for the inventory list view
    path('', views.inventory_list, name='inventory-list'),
    
    # URL pattern for the user registration view
    path('register/', views.register, name='register'),
    
    # URL pattern for the user login view
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    
    # URL pattern for the user logout view
    path('logout/', auth_views.LogoutView.as_view(
        template_name='registration/logged_out.html',
        next_page='login'
    ), name='logout'),
    
    # URL pattern for the inventory detail view
    path('inventory/<int:pk>/', views.inventory_detail, name='inventory-detail'),
    
    # URL pattern for creating a new inventory item
    path('inventory/new/', views.inventory_create, name='inventory-create'),
    
    # URL pattern for updating an existing inventory item
    path('inventory/<int:pk>/edit/', views.inventory_update, name='inventory-update'),
    
    # URL pattern for deleting an existing inventory item
    path('inventory/<int:pk>/delete/', views.inventory_delete, name='inventory-delete'),
]
