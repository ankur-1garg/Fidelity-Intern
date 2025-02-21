from django.db import models

# Create your models here.


class Price(models.Model):
    item = models.CharField(max_length=100)
    item_id = models.IntegerField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.item} (ID: {self.item_id}) - ${self.price}"
