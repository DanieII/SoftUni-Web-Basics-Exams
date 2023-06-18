from django.urls import path, include

from photos.views import photo_details, add_photo, edit_photo, delete_photo

urlpatterns = [
    path('add/', add_photo, name='add photo'),
    path('<int:pk>', include([
        path('', photo_details, name='photo details'),
        path('edit/', edit_photo, name='edit photo'),
        path('delete/', delete_photo, name='delete photo'),
    ])),
]
