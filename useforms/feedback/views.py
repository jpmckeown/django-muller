from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm 

# Forms class way
def review(request):
    form = ReviewForm()

    return render(request, 'feedback/feedback.html')


# manual way
def feedback(request):
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