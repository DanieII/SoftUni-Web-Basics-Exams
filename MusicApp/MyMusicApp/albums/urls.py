from django.urls import path, include

from albums.views import home, add_album, album_details, edit_album, delete_album

urlpatterns = [
    path('', home, name='home'),
    path('album/', include([
        path('add/', add_album, name='add album'),
        path('detals/<int:pk>/', album_details, name='album details'),
        path('edit/<int:pk>/', edit_album, name='edit album'),
        path('delete/<int:pk>/', delete_album, name='delete album'),
    ]))
]
