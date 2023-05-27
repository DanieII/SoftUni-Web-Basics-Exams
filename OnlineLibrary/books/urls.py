from django.urls import path

from books.views import home, add_book, book_details, edit_book, delete_book

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_book, name='add book'),
    path('details/<int:id>/', book_details, name='book details'),
    path('edit/<int:id>/', edit_book, name='edit book'),
    path('delete/<int:id>/', delete_book, name='delete book'),
]
