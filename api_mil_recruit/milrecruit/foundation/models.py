from django.db import models

# Create your models here.
class MilitaryDb(models.Model):
    member_name = models.CharField(max_length = None),
    age = models.PositiveSmallIntegerField()
    has_glasses = models.BooleanField()
    name = models.CharField(max_length = 20)

    def __str__(self):
        return str(self.member_name)+"age:  " + str(self.age)+ ",has glasses: " +str(self.has_glasses)
