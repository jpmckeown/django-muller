from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.edit import FormView, CreateView
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from .forms import ReviewForm
from .models import Review


# class expecting a model
class ReviewsListView(ListView):
    template_name = "feedback/review_list.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        base = super().get_queryset()
        data = base.filter(rating__lt=3)
        return data


class DetailsView(DetailView):
    template_name = "feedback/one_review.html"
    model = Review


class DetailsViewT(TemplateView):
    template_name = "feedback/one_review.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        one_review = Review.objects.get(pk=review_id)
        context["review"] = one_review
        return context


class ReviewsListViewT(TemplateView):
    template_name = "feedback/review_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context


class ThanksView(TemplateView):
    template_name = "feedback/thanks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Its going well"
        return context


class ThankyouView(View):
    def get(self, request):
        return render(request, "feedback/thanks.html")


def thanks(request):
    return render(request, "feedback/thanks.html")


# doesnt need a matching class in forms.py, infers from model
# optionally can set form_clas to a ModelForm
class FeedbackView(CreateView):
    model = Review
    fields = "__all__"
    template_name = "feedback/feedback.html"
    success_url = "/thanks/"


# must use a class in forms.py
class FeedbackFormView(FormView):
    form_class = ReviewForm
    template_name = "feedback/feedback.html"
    success_url = "/thanks/"

    # method only runs when valid form received - its not a validator!
    def form_valid(self, form: ReviewForm) -> HttpResponse:
        form.save()
        response = super().form_valid(form)
        return response


class FeedbackViewV(View):
    def get(self, request):
        # make new empty form
        form = ReviewForm()
        return render(
            request,
            "feedback/feedback.html",
            {
                "form": form,
            },
        )

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thanks/")
        return render(
            request,
            "feedback/feedback.html",
            {
                "form": form,
            },
        )


# ModelForm way
def feedback(request):
    if request.method == "POST":
        # here after a form was submitted with data
        # how to edit existing object
        existing_data = Review.objects.get(pk=3)
        form = ReviewForm(request.POST, instance=existing_data)

        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect("/thanks/")

    else:
        # make new empty form
        form = ReviewForm()

    return render(
        request,
        "feedback/feedback.html",
        {
            "form": form,
        },
    )


# forms.Form class way
def feedback_form(request):
    if request.method == "POST":
        # here after a form was submitted with data
        form = ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            review = Review(
                user_name=form.cleaned_data["user_name"],
                review_text=form.cleaned_data["review_text"],
                rating=form.cleaned_data["rating"],
            )
            review.save()
            return HttpResponseRedirect("/thanks/")

    else:
        # make new empty form
        form = ReviewForm()

    return render(
        request,
        "feedback/feedback.html",
        {
            "form": form,
        },
    )


# manual way
def feedback_manual(request):
    if request.method == "POST":
        # request holds a dictionary
        entered_username = request.POST["username"]

        if entered_username == "":
            return render(request, "feedback/feedback.html", {"has_error": True})

        print(entered_username)
        return HttpResponseRedirect("/thanks/")

    return render(request, "feedback/feedback.html", {"has_error": False})
