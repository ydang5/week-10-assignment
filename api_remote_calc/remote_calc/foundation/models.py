from django.db import models

# Create your models here.
class Memory(models.Model):
    saved_data = models.FloatField()
