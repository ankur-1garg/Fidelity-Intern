from django.db import models

class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    pickup_datetime = models.DateTimeField()
    dropoff_datetime = models.DateTimeField()
    passenger_count = models.IntegerField()
    trip_distance = models.DecimalField(max_digits=10, decimal_places=2)
    fare_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tip_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pickup_location = models.CharField(max_length=100)
    dropoff_location = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'TRIPS'  # Snowflake table name (usually uppercase)
        
    def __str__(self):
        return f"Trip {self.trip_id} - {self.pickup_datetime}"
