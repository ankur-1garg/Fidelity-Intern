from django.db import models


class Orders(models.Model):
    order_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    email = models.EmailField()
    addr = models.TextField(max_length=200)

    def __str__(self):
        return self.name
