from django.db import models
from django.core.validators import MinLengthValidator


class Location(models.Model):
    pincode = models.CharField(
        primary_key=True,
        max_length=6,
        validators=[MinLengthValidator(6)]
    )
    district = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)]
    )
    state = models.CharField(max_length=50)
    population_density = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text="Population per square km"
    )
    district_headquarters = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['state', 'district']
        unique_together = ['district', 'state']
        indexes = [
            models.Index(fields=['last_updated']),
        ]

    def __str__(self):
        return f"{self.district}, {self.state} ({self.pincode})"
