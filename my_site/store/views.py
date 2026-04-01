from django.shortcuts import render
from django.http import Http404
from .models import Book

def index(request):
    allbooks = Book.objects.all()
    return render(request, 'store/index.html', {
        'books': allbooks
    })

def detail(request, id):
    try:
        book = Book.objects.get(pk=id)
    except:
        raise Http404()
    return render(request, 'store/book_detail.html', {
        'book': book,
        'title': book.title,
    })