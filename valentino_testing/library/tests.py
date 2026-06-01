from django.test import TestCase
from library.models import Author, Book, Event, Contact
from model_bakery import baker


class TestContactForm(TestCase):
    def test_can_send_message(self):
        data = {
            "first_name": "Juliana",
            "last_name": " Crain",
            "message": "Would love to talk about Philip K. Dick",
        }
        response = self.client.post("/contact/", data=data)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertRedirects(response, "/thanks/")


class TestEventModel(TestCase):
    def test_event_model(self):
        event = baker.make(Event, title="The man in the high castle presentation")
        self.assertEqual(str(event), "The man in the high castle presentation")


# 2 models so not a unit test; an integration test
class TestBookAuthorModels(TestCase):
    def test_book_has_an_author(self):
        book = Book.objects.create(title="The man in the high castle")
        philip = Author.objects.create(first_name="Philip", last_name="K. Dick")
        book.authors.set([philip.pk])
        self.assertEqual(book.authors.count(), 1)
