from django.urls import path, include

from photos.views import photo_details

urlpatterns = [
    # path('add/', add_photo, name='add photo'),
    path('<int:pk>', include([
        path('', photo_details, name='photo details'),
    #     path('edit/', edit_photo, name='edit photo'),
    ])),
]
