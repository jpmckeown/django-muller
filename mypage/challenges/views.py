from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly = {
    "jan": "Januaury is coolest",
    "feb": "February is friendly",
    "mar": "March can be rainy",
    "apr": "April is a new life at Easter",
    "may": "May is often pleasant when sunny",
    "jun": "June is too hot in afternoon",
    "jul": "July is often too hot in morning",
    "aug": "August may be too hot in afternoon",
    "sep": "September is usually pleasant"
}


# dict is ordered by default since Python>3.6
def month_by_number(request, month):
    months = list(monthly.keys())
    fwd_month = months[month]
    return HttpResponseRedirect("/challenges/" + fwd_month)


def month_by_name(request, month):
    try:
        msg = monthly[month]
        return HttpResponse(msg)
    except:
        return HttpResponseNotFound("Month not recognised")


def index(request):
    return HttpResponse("working!")
