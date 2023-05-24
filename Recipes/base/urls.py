from django.urls import path

from base.views import home, create_recipe, edit_recipe, delete_recipe, recipe_details

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_recipe, name='create'),
    path('edit/<int:id>/', edit_recipe, name='edit'),
    path('delete/<int:id>/', delete_recipe, name='delete'),
    path('details/<int:id>/', recipe_details, name='details')
]
