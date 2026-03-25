# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    if month > len(months):
        return HttpResponseNotFound(f"Invalid month number {month}")
    fwd_month = months[month - 1]
    fwd_path = reverse("monthly", args=[fwd_month])
    return HttpResponseRedirect(fwd_path)


def month_by_name(request, month):
    try:
        msg = monthly[month]
        response_data = f"<h1>{msg}</h1>"
        return HttpResponse(response_data)
    except ValueError:
        return HttpResponseNotFound("Month not recognised")


def index(request):
    return HttpResponse("working!")
