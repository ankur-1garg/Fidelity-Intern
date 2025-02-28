from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductListView, ProductDetailView

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('api/', include(router.urls)),
]
