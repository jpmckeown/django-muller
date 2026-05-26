from django.db import models

class Review(models.Model):
    user_name = models.CharField(max_length=40)
    review_text = models.CharField(max_length=200)
    rating = models.IntegerField()
