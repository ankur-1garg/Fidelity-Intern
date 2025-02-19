from django.db import models

# Create your models here.

class employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.IntegerField()
    salary = models.IntegerField()
    doj = models.DateField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "employee"
    