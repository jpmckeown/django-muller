from django.urls import path

from . import views

urlpatterns = [
    path("profiles/", views.CreateProfileView.as_view()),
    path("profiles/list", views.ListProfilesView.as_view()),
]
