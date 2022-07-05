from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=120)
    desc = models.TextField()

class Score(models.Model):
    username = models.CharField(max_length=122)
    moves = models.IntegerField()
    time = models.CharField(max_length=100)