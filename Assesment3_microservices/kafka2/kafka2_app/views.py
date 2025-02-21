from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Location
from .serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Location instances.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    lookup_field = 'pincode'  # Use pincode as the lookup field since it's our primary key

    def get_queryset(self):
        """
        Optionally restricts the returned locations by filtering against
        query parameters in the URL.
        """
        queryset = Location.objects.all()
        state = self.request.query_params.get('state', None)
        district = self.request.query_params.get('district', None)

        if state:
            queryset = queryset.filter(state__icontains=state)
        if district:
            queryset = queryset.filter(district__icontains=district)

        return queryset.order_by('state', 'district')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
