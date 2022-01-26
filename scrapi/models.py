from django.db import models

# Create your models here.
class Details(models.Model):
    Company = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    Designation = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)