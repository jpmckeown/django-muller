from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
import re


class Country(models.Model):
    name = models.CharField(max_length=80)
    iso = models.CharField(max_length=3)


class Library(models.Model):
    curator = models.CharField(max_length=80)
    established = models.DateField()

    def __str__(self):
        return f"{self.curator} since {self.established}"
    
    class Meta:
        verbose_name_plural = "Museum"


class Author(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    library = models.OneToOneField(Library, null=True, on_delete=models.SET_NULL)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def last_name_first(self):
        return f"{self.last_name}, {self.first_name}"

    def __str__(self):
        return self.last_name_first()


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name="books")
    location = models.ManyToManyField(Country)
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
        if not self.slug:
            self.slug = self.slugify_skip_the(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title}, by {self.author.first_name} {self.author.last_name} ({self.rating}) {self.slug}"
