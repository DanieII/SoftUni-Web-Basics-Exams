from django.urls import path, include

from pets.views import pet_details

urlpatterns = [
    # path('add/', add_pet, name='add pet'),
    path('<username>/pet/<slug:pet_slug>', include([
        path('', pet_details, name='pet details'),
    #     path('edit/', edit_pet, name='edit pet'),
    #     path('delete/', delete_pet, name='delete pet'),
    #     path('delete/', delete_pet, name='delete pet'),
    ])),
]
