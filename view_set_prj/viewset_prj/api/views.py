from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import F1Driver
from .serializer import F1DriverSerializer

class F1DriverViewSet(viewsets.ViewSet):
    def list(self, request):
        """List all F1 drivers"""
        drivers = F1Driver.objects.all()
        serializer = F1DriverSerializer(drivers, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Retrieve a specific F1 driver"""
        driver = get_object_or_404(F1Driver, pk=pk)
        serializer = F1DriverSerializer(driver)
        return Response(serializer.data)

    def create(self, request):
        """Create a new F1 driver"""
        serializer = F1DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """Update an existing F1 driver"""
        driver = get_object_or_404(F1Driver, pk=pk)
        serializer = F1DriverSerializer(driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        """Partially update an F1 driver"""
        driver = get_object_or_404(F1Driver, pk=pk)
        serializer = F1DriverSerializer(driver, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Delete an F1 driver"""
        driver = get_object_or_404(F1Driver, pk=pk)
        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

