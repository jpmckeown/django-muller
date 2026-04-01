from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
import re

class Book(models.Model):
    author = models.CharField(null=True, max_length=50)
    title = models.CharField(max_length=50)
    rating = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    slug = models.SlugField(default='', null=False)
    # id = models.AutoField() # automatically added by Django

    @staticmethod
    def slugify_skip_the(title: str) -> str:
        stripped = re.sub(r'^the\s+', '', title, flags=re.IGNORECASE)
        return slugify(stripped)
    
    def get_absolute_url(self):
        return reverse("detail", args=[self.id])
    # reverse("model_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        self.slug = self.slugify_skip_the(self.title)
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.rating}) {self.slug}"
