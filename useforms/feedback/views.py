from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm
from .models import Review


# ModelForm way
def feedback(request):
    if request.method == "POST":
        # here after a form was submitted with data
        form = ReviewForm(request.POST)

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


def thanks(request):
    return render(request, "feedback/thanks.html")
