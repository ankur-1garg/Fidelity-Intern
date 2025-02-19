from django.urls import path
from . import views

urlpatterns = [
    # Function-based URLs
    path('managers/', views.manager_list, name='manager_list'),
    path('manager/<int:employee_id>/', views.manager_detail, name='manager_detail'),
    
    # Class-based URLs
    path('cbv/managers/', views.ManagerListView.as_view(), name='cbv_manager_list'),
]