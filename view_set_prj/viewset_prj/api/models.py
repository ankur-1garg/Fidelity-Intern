from django.db import models


class F1Driver(models.Model):
    driver_name = models.CharField(max_length=100)
    # e.g., Mercedes, Red Bull, Ferrari
    team = models.CharField(max_length=100)
    car_number = models.IntegerField(unique=True)
    championship_points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.driver_name} - {self.team} (#{self.car_number})"

    class Meta:
        # Orders by points in descending order
        ordering = ['-championship_points']
