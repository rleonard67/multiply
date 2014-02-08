from django.db import models

# Create your models here.

class Quizzes(models.Model):
    id = models.AutoField(primary_key=True)
    quizdate = models.DateField()
    score = models.IntegerField()