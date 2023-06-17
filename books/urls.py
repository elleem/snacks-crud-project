from django.urls import path
from .views import BookListView, BookDetailView, AboutView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/delete', BookDeleteView.as_view(), name='book_delete'),
    path('<int:pk>/update', BookUpdateView.as_view(), name='book_update'),
    path('about', AboutView.as_view(), name='about'),
]