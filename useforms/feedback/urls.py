from django.urls import path
from . import views

urlpatterns = [
    path("", views.FeedbackView.as_view()),
    # path("", views.feedback),
    path("thanks/", views.ThanksView.as_view()),
]
