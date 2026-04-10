from django.contrib import admin
from .models import Author, Post, Tag

class AuthorAdmin(admin.ModelAdmin):

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)

CLASS

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Tag)
