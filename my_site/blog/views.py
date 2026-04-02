from django.http import HttpResponse
from django.shortcuts import render

# a view must return an HttpResponse not a string
def index(request):
    return render(request, 'blog/index.html')
    # return HttpResponse('index')

def post(request):
    return HttpResponse('one post')
