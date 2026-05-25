from django import forms

class ReviewForm(forms.Form):
    user_name_form = forms.CharField(label="Your name", max_length=30, error_messages={
        "required": "Your username should not be blank.",
        "max_length": "Your username should not exceed 20 characters length.",
    })
