from django.urls import path, include

from plants.views import home, catalogue, create_plant, plant_details, edit_plant, delete_plant

urlpatterns = [
    path('', include([
        path('', home, name='home'),
        path('catalogue/', catalogue, name='catalogue'),
        path('create/', create_plant, name='create plant'),
    ])),
    path('details/<int:pk>/', plant_details, name='plant details'),
    path('edit/<int:pk>/', edit_plant, name='edit plant'),
    path('delete/<int:pk>/', delete_plant, name='delete plant'),
]
