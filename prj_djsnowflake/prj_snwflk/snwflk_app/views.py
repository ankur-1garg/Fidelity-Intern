from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Avg, Sum
from datetime import datetime
from .models import Trip
from .serializer import TripSerializer


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['pickup_location', 'dropoff_location', 'payment_type']
    ordering_fields = ['pickup_datetime', 'total_amount', 'trip_distance']

    @action(detail=False, methods=['get'])
    def stats(self, request):
        """Get trip statistics"""
        stats = self.get_queryset().aggregate(
            avg_fare=Avg('fare_amount'),
            avg_distance=Avg('trip_distance'),
            total_revenue=Sum('total_amount')
        )
        return Response(stats)

    @action(detail=True, methods=['get'])
    def trip_details(self, request, pk=None):
        trip = get_object_or_404(Trip, pk=pk)
        data = {
            'pickup_location': trip.pickup_location,
            'dropoff_location': trip.dropoff_location,
            'pickup_datetime': trip.pickup_datetime
        }
        return Response(data)

    @action(detail=False, methods=['get'])
    def all_trip_details(self, request):
        trips = self.get_queryset().values(
            'pickup_location',
            'dropoff_location',
            'pickup_datetime'
        )
        return Response(trips)

    @action(detail=False, methods=['get'])
    def trips_by_date(self, request):
        """Get all trips for a specific date"""
        date_str = request.query_params.get('date')

        if not date_str:
            return Response(
                {"error": "Date parameter is required (format: YYYY-MM-DD)"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            trips = self.get_queryset().filter(
                pickup_datetime__date=date.date()
            ).values(
                'trip_id',
                'pickup_location',
                'dropoff_location',
                'pickup_datetime',
                'fare_amount',
                'total_amount'
            )

            if not trips:
                return Response(
                    {"message": f"No trips found for date {date_str}"},
                    status=status.HTTP_404_NOT_FOUND
                )

            summary = {
                "date": date_str,
                "total_trips": len(trips),
                "total_revenue": sum(trip['total_amount'] for trip in trips),
                "trips": list(trips)
            }

            return Response(summary)

        except ValueError:
            return Response(
                {"error": "Invalid date format. Use YYYY-MM-DD"},
                status=status.HTTP_400_BAD_REQUEST
            )
