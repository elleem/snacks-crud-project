from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Book

class BookListView(ListView):
    template_name = "book_list.html"
    model = Book
    context_object_name = "books"

class BookDetailView(DetailView):
    template_name = "book_detail.html"
    model = Book

class BookCreateView(CreateView):
    template_name = "book_create.html"
    model = Book
    fields = ["title", "purchaser", "description", "image_url"]

class BookDeleteView(DeleteView):
    template_name = "book_delete.html"
    model = Book
    success_url = reverse_lazy("book_list")

class BookUpdateView(UpdateView):
    template_name = "book_update.html"
    model = Book
    fields = "__all__"

class AboutView(TemplateView):
    template_name = "about.html"

