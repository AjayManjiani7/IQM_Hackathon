from django.db import models
import uuid
import datetime
from django.conf import settings

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name


class Department_user(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.department + " " + self.role