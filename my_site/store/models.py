from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
import re

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(null=True, max_length=50)
    rating = models.IntegerField(null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    slug = models.SlugField(default='', null=False, blank=True)
    # id = models.AutoField() # automatically added by Django

    _TITLE_CASE_EXCEPTIONS = {
        'a', 'an', 'the', 'and', 'but', 'or', 'nor', 'for', 'so', 'yet',
        'at', 'by', 'in', 'of', 'on', 'to', 'up', 'as',
    }

    @staticmethod
    def slugify_skip_the(title: str) -> str:
        stripped = re.sub(r'^the\s+', '', title, flags=re.IGNORECASE)
        return slugify(stripped)

    def apply_title_case(self, title: str) -> str:
        words = title.split()
        return ' '.join(
            word.capitalize() if i == 0 or word.lower() not in self._TITLE_CASE_EXCEPTIONS
            else word.lower()
            for i, word in enumerate(words)
        )

    def get_absolute_url(self):
        return reverse("detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.title = self.apply_title_case(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title}, by {self.author}. ({self.rating}) {self.slug}"
