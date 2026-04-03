from django.shortcuts import render
from django.http import Http404
from django.db.models import Avg, Min
from .models import Book

def index(request):
    allbooks = Book.objects.all()
    num_books = allbooks.count()
    avg_rating = allbooks.aggregate(Avg('rating'), Min('rating'))
    return render(request, 'store/index.html', {
        'books': allbooks,
        "total_number_of_books": num_books,
        "average_rating": avg_rating
    })

def detail(request, slug):
    try:
        book = Book.objects.get(slug=slug)
    except:
        raise Http404()
    return render(request, 'store/book_detail.html', {
        'book': book,
        'title': book.title,
    })