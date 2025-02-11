from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone


class Employee(AbstractUser):
    employee_id = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    date_of_joining = models.DateField()

    # Add related_name attributes to avoid conflicts
    groups = models.ManyToManyField(Group, related_name='employee_set')
    user_permissions = models.ManyToManyField(
        Permission, related_name='employee_set')

    USERNAME_FIELD = 'employee_id'
    REQUIRED_FIELDS = ['email', 'date_of_joining', 'username']

    def __str__(self):
        return f"{self.username} ({self.employee_id})"
