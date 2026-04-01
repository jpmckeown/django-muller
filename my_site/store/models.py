from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    author = models.CharField(null=True, max_length=50)
    title = models.CharField(max_length=50)
    rating = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    # id = models.AutoField() # automatically added by Django

    def __str__(self):
        return f"{self.title} by {self.author} ({self.rating})"
