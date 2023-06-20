from django.urls import path

from plants.views import home, catalogue, create_plant, plant_details, edit_plant, delete_plant

urlpatterns = [
    path('', home, name='home'),
    path('catalogue/', catalogue, name='catalogue'),
    path('create/', create_plant, name='create plant'),
    path('details/<int:plant_id>/', plant_details, name='plant details'),
    path('edit/<int:plant_id>/', edit_plant, name='edit plant'),
    path('delete/<int:plant_id>/', delete_plant, name='delete plant'),
]
