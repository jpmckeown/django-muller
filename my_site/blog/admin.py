from django.contrib import admin
from .models import Author, Post, Tag

class AuthorAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Tag)
