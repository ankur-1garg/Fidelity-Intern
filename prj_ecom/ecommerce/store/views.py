from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from bson import ObjectId
from .models import Product
from .serializers import ProductSerializer
from django.views.generic import ListView, DetailView


class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for basic CRUD operations on Products:
    - List all products (GET /api/products/)
    - Create new product (POST /api/products/)
    - Retrieve a product (GET /api/products/{id}/)
    - Update a product (PUT /api/products/{id}/)
    - Delete a product (DELETE /api/products/{id}/)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ['name', 'price']
    search_fields = ['name', 'description']
    ordering_fields = ['price']

    def get_permissions(self):
        """Allow anyone to view products, require authentication for other actions"""
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        """List all products with optional filtering"""
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """Create a new product"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        """Retrieve a specific product"""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """Update a specific product"""
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """Delete a specific product"""
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def mark_featured(self, request, pk=None):
        product = self.get_object()
        product.is_featured = True
        product.save()
        serializer = self.get_serializer(product)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def in_stock(self, request):
        in_stock = self.get_queryset().filter(stock__gt=0)
        page = self.paginate_queryset(in_stock)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(in_stock, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['delete'])
    def delete_by_mongo_id(self, request):
        """Delete a product using MongoDB ObjectID"""
        mongo_id = request.query_params.get('mongo_id')
        if not mongo_id:
            return Response(
                {'error': 'mongo_id is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            # Get the product first to verify it exists
            product = Product.objects.get(_id=ObjectId(mongo_id))
            product.delete()
            return Response(
                {'message': f'Product with ID {mongo_id} deleted successfully'},
                status=status.HTTP_204_NO_CONTENT
            )
        except Product.DoesNotExist:
            return Response(
                {'error': f'Product with ID {mongo_id} not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    def get_queryset(self):
        """Custom queryset with price filtering"""
        queryset = Product.objects.all()
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if min_price:
            queryset = queryset.filter(price__gte=float(min_price))
        if max_price:
            queryset = queryset.filter(price__lte=float(max(max_price)))

        return queryset


class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'
    context_object_name = 'product'
