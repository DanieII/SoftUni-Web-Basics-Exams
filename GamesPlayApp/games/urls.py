from django.urls import path, include

from games.views import home, dashboard, create_game, game_details, edit_game, delete_game

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('game/', include([
        path('create/', create_game, name='crate game'),
        path('details/<int:pk>/', game_details, name='game details'),
        path('edit/<int:pk>/', edit_game, name='edit game'),
        path('delete/<int:pk>/', delete_game, name='delete game'),
    ]))
]
