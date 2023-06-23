from django.urls import path

from profiles.views import create_profile, profile_details, delete_profile

urlpatterns = [
    path('create-profile', create_profile, name='create profile'),
    path('details', profile_details, name='profile details'),
    path('delete', delete_profile, name='delete profile'),
]
