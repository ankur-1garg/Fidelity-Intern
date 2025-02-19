from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.IntegerField()
    salary = models.IntegerField()
    doj = models.DateField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True
    
class Manager(CommonInfo):  # Inherits from CommonInfo, not models.Manager
    manages = models.IntegerField()  # Number of employees managed
    
    class Meta:
        db_table = 'manager'
