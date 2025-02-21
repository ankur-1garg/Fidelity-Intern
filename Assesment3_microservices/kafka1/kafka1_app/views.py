from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
import requests
from .models import Price
from .serializers import PriceSerializer


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    lookup_field = 'item_id'

    @action(detail=False, methods=['get'])
    def combined_data(self, request):
        # Fetch prices from current system
        prices = Price.objects.all()
        prices_data = PriceSerializer(prices, many=True).data

        try:
            # Try to fetch locations from Kafka2
            locations_response = requests.get(
                'http://127.0.0.1:8001/api/locations/',
                timeout=3  # Add timeout to avoid long waiting
            )
            locations_data = locations_response.json()

            # Return combined data if locations are available
            return Response({
                'status': 'success',
                'locations': locations_data,
                'prices': prices_data
            })

        except requests.RequestException:
            # Return only prices if location service is unavailable
            return Response({
                'status': 'partial_success',
                'message': 'Location service is unavailable',
                'prices': prices_data
            })

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
