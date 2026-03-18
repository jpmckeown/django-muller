from django.urls import path
from . import views
urlpatterns = [
    path("<month>", views.monthly),
    path("january", views.index),
    path("february", views.ifeb)
]