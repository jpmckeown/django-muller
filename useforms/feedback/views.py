from django.shortcuts import render
from django.http import HttpResponseRedirect


def feedback(request):
    if request.method == 'POST':
        # request holds a dictionary
        entered_username = request.POST['username']

        if entered_username=="":
            return render(request, 'feedback/feedback.html', {"has_error": True})

        print(entered_username)
        return HttpResponseRedirect("/thanks/")
    
    return render(request, 'feedback/feedback.html')


def thanks(request):
    return render(request, 'feedback/thanks.html', {"has_error": False})