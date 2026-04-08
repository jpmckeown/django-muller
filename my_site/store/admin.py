from django.contrib import admin
from .models import Book, Author, Library, Country

class BookAdmin(admin.ModelAdmin):
    list_filter = ('author', 'rating',)
    list_display = ('title', 'author', 'rating', 'slug')
    filter_horizontal = ('location',)
    class Media:
        js = ('store/admin_book.js',)
    
    # prepopulated_fields = {'slug': ('title',)}  # replaced by custom JS (strips leading "the")
    # readonly_fields = ('slug',)  # earlier approach but if readonly cannot prepopulate


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Country)
