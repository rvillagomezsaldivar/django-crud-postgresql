from django.db import models

# Create your models here.
class Campus(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)

