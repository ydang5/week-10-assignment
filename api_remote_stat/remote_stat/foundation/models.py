from django.db import models

# Create your models here.
class Memory(models.Model):
    value = models.FloatField()
