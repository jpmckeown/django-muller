from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly = {
    "jan": "No wokery here!",
    "feb": "British and proud",
    "mar": "Make Britain Great Again"
}

# dict is ordered by default since Python>3.6
def month_by_number(request, month):
    return HttpResponse(month)

def month_by_name(request, month):
    try:
        msg = monthly[month]
        return HttpResponse(msg)
    except:
        return HttpResponse("Month not recognised")

def month_manual(request, month):
    if month == "january":
        msg = "Jan working!"
    elif month == "february":
        msg = "fish today"
    else:
        return HttpResponseNotFound("Not Found")
    return HttpResponse(msg)

def index(request):
    return HttpResponse("working!")
def ifeb(request):
    return HttpResponse("February content")