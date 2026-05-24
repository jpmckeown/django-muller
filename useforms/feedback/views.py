from django.shortcuts import render
from django.http import HttpResponseRedirect

def feedback(request):
    if request.method == 'POST':
        entered_username = request.POST['username']
        print(entered_username)
        return HttpResponseRedirect("/thanks/")
    
    return render(request, 'feedback/feedback.html')

def thanks(request):
    return render(request, 'feedback/thanks.html')