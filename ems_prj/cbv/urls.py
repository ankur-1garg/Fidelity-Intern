from django.urls import path
from . import views

app_name = 'cbv'

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('product/add/', views.ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(),
         name='product-detail'),
    path('products/<str:name>/', views.ProductDetailView.as_view(),
         name='product-detail-by-name'),
    path('cbv/', views.MyClass.as_view()),
    path('product/<int:pk>/delete/',
         views.ProductDeleteView.as_view(), name='product-delete'),
]
