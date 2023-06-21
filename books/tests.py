from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Book


class BookTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.book = Book.objects.create(
            name="pickle", purchaser=self.user, description="pickle description",
            image_url="http://pickel-image-url.com"
        )

    def test_string_representation(self):
        self.assertEqual(str(self.book), "pickle")

    def test_book_content(self):
        self.assertEqual(f"{self.book.name}", "pickle")
        self.assertEqual(f"{self.book.purchaser}", "tester")
        self.assertEqual(self.book.description, "pickle description")

    def test_book_list_view(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "pickle")
        self.assertTemplateUsed(response, "book_list.html")

    def test_book_detail_view(self):
        response = self.client.get(reverse("book_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Purchaser: tester")
        self.assertTemplateUsed(response, "book_detail.html")

    def test_book_create_view(self):
        response = self.client.post(
            reverse("book_create"),
            {
                "name": "Rake",
                "purchaser": self.user.id,
                "description": "test description",
                "image_url" : "https://upload.wikimedia.org/wikipedia/commons/b/bb/Pickle.jpg",
            },
            follow=True
        )
        self.assertRedirects(response, reverse("book_detail", args="2"))
        self.assertContains(response, "Rake")

    def test_book_update_view_redirect(self):
        response = self.client.post(
            reverse("book_update", args="1"),
            {"name": "Updated name", "purchaser": self.user.id, "description": "test description",
             "image_url": "testimageurl.com"}
        )

        self.assertRedirects(response, reverse("book_detail", args="1"), target_status_code=200)

    def test_book_update_bad_url(self):
        response = self.client.post(
            reverse("book_update", args="1"),
            {"name": "Updated name", "purchaser": self.user.id, "description": "test description",
             "image_url": "badurl"}
        )

        self.assertEqual(response.status_code, 200)

    def test_book_delete_view(self):
        response = self.client.get(reverse("book_delete", args="1"))
        self.assertEqual(response.status_code, 200)

    # you can also tests models directly
    def test_model(self):
        book = Book.objects.create(name="rake", purchaser=self.user)
        self.assertEqual(book.name, "rake")