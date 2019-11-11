from django.db import models

# Create your models here.
class StudentDb(models.Model):
    # name = models.CharField(max_length = 50),
    student_number = models.PositiveSmallIntegerField()
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return "student number: " + str(self.student_number)+ ",age: " +str(self.age)
