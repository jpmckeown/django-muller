from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def monthly(request, month):
    if month == "january":
        msg = "Jan working!"
    elif month == "february":
        msg = "fish today"
    else:
        return HttpResponseNotFound
    return HttpResponse(msg)

def index(request):
    return HttpResponse("working!")
def ifeb(request):
    return HttpResponse("February content")