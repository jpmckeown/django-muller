from django.conf.urls.i18n import urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path("contact/", views.ContactView.as_view()),
    path("thanks/", views.ThanksView.as_view()),
]
