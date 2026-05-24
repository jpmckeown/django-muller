from django.urls import path
from . import views

urlpatterns = [
    path("", views.feedback),
    path("thanks/", views.thanks)
]