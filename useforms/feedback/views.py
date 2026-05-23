from django.shortcuts import render

def feedback(request):
    return render(request, 'feedback/feedback.html')
