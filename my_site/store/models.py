from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    # id = models.AutoField() # automatically added by Django
