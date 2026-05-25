from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm 

# Forms class way
def feedback(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thanks/")

    else:
        # make new empty form
        form = ReviewForm()

    return render(request, 'feedback/feedback.html', {
        "form": form,
    })


# manual way
def feedback_manual(request):
    if request.method == 'POST':
        # request holds a dictionary
        entered_username = request.POST['username']

        if entered_username=="":
            return render(request, 'feedback/feedback.html', {"has_error": True})

        print(entered_username)
        return HttpResponseRedirect("/thanks/")
    
    return render(request, 'feedback/feedback.html', {"has_error": False})


def thanks(request):
    return render(request, 'feedback/thanks.html')