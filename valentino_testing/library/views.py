from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import Contact
from .forms import ContactForm


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "library/contact.html"
    success_url = "/thanks/"


class ThanksView(TemplateView):
    template_name = "library/thanks.html"
