from django.urls import path
from . import views

urlpatterns = [
    path("", views.FeedbackView.as_view()),
    # path("", views.feedback),
    path("thanks/", views.ThanksView.as_view()),
    path("reviews/", views.ReviewsListView.as_view()),
    path("reviews/favourite", views.AddFavouriteView.as_view()),
    # DetailView version
    path("reviews/<int:pk>", views.DetailsView.as_view(), name="one_review"),
    # TemplateView version
    # path("reviews/<int:id>", views.DetailsView.as_view(), name="one_review"),
]
