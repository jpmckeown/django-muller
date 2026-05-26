from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your name", max_length=30, error_messages={
        "required": "Your username should not be blank.",
        "max_length": "Your username should not exceed 20 characters length.",
    })
    review_text = forms.CharField(label="Feedback", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Rating", min_value=1, max_value=5)
