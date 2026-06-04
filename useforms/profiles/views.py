from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .forms import ProfileForm
from .models import UserProfile


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm
        # form = self.form()
        return render(request, "profiles/create_profile.html", {"form": form})

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            profile = UserProfile(image=request.FILES["user_image"])
            profile.save()
            # store_file(request.FILES["image"])
            # print(request.FILES["image"])
            return HttpResponseRedirect("/profiles")

        return render(request, "profiles/create_profile.html", {"form": submitted_form})


def store_file(file):
    with open("temp/pic.png", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileViewManually(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        store_file(request.FILES["image"])
        print(request.FILES["image"])
        return HttpResponseRedirect("/profiles")
