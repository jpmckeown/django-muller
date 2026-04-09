from django.db import models

class Author(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)

    def __str__(self):
        return f"{self.first} {self.last} {self.email}"

class Post(models.Model):
    title = models.CharField(max_length=80)
    excerpt = models.CharField(max_length=120)
    image = models.CharField(max_length=80)
    date = models.DateField()
    slug = models.CharField(max_length=80)
    content = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.title}"

class Tag(models.Model):
    caption = models.CharField(max_length=40)

