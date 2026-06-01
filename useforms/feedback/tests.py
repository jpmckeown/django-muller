from django.test import TestCase
from .forms import ReviewForm


class TestReviewForm(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.valid_data = {
            "user_name": "Alice",
            "review_text": "Great service",
            "rating": 4,
        }

    def test_valid_form(self):
        form = ReviewForm(
            data={
                "user_name": "Alice",
                "review_text": "Great service",
                "rating": 4,
            }
        )
        self.assertTrue(form.is_valid())

    def test_missing_user_name(self):
        form = ReviewForm(
            data={
                "user_name": "",
                "review_text": "Great service",
                "rating": 4,
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("user_name", form.errors)

    def test_custom_error_message(self):
        form = ReviewForm(
            data={
                "user_name": "",
                "review_text": "Great service",
                "rating": 4,
            }
        )
        form.is_valid()
        self.assertIn("dont be missing!", form.errors["user_name"])

    def test_missing_review_text(self):
        form = ReviewForm(
            data={
                "user_name": "Alice",
                "review_text": "",
                "rating": 4,
            }
        )
        self.assertFalse(form.is_valid())

    def test_missing_rating(self):
        form = ReviewForm(
            data={
                "user_name": "Alice",
                "review_text": "Great service",
                "rating": "",
            }
        )
        self.assertFalse(form.is_valid())
