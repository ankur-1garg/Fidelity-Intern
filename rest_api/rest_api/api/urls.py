from django.urls import path
from . import views

urlpatterns = [
    # path('', views.api_overview, name='api-overview'),
    # Add more URL patterns as needed
    path("data/", views.get_data, name='get-data'),
    path("create-student/", views.create_student, name='create-student'),
    path("get-students/", views.get_students, name='get-students'),
    path("get-student/<str:pk>/", views.get_student, name='get-student-id'),
    path("update-student/<str:pk>/", views.student_update, name='update-student'),
    path("delete-student/<str:pk>/", views.student_delete, name='delete-student'),
]
