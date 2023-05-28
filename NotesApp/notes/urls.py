from django.urls import path

from notes.views import home, add_note, edit_note, delete_note, details_note

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_note, name='add note'),
    path('edit/<int:id>/', edit_note, name='edit note'),
    path('delete/<int:id>/', delete_note, name='delete note'),
    path('details/<int:id>/', details_note, name='details note'),
]
