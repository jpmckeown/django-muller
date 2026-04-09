from django.db import models
from django.core.validators import MinLengthValidator


class Author(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)

    def __str__(self):
        return f"{self.first} {self.last} {self.email}"


class Tag(models.Model):
    caption = models.CharField(max_length=40)


class Post(models.Model):
    title = models.CharField(max_length=80)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=80)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True, max_length=80)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(to=Author, null=True, on_delete=models.SET_NULL, related_name="posts")
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"{self.title}"
