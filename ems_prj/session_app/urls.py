from django.urls import path
from . import views

app_name = 'session_app'

urlpatterns = [
    path('', views.session_home, name='session_home'),
    path('set/', views.set_session, name='set_session'),
    path('get/', views.get_session, name='get_session'),
    # path('delete/', views.delete_session, name='delete_session'),
]
