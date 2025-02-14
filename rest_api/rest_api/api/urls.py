from django.urls import path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Students API",
        default_version='v1',
        description="API for managing student records",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@students.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # API endpoints
    path('data/', views.get_data, name='get-data'),
    path('create-student/', views.create_student, name='create-student'),
    path('get-students/', views.get_students, name='get-students'),
    path('get-student/<str:pk>/', views.get_student, name='get-student-id'),
    path('update-student/<str:pk>/', views.student_update, name='update-student'),
    path('delete-student/<str:pk>/', views.student_delete, name='delete-student'),

    # Documentation endpoints
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('openapi/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
