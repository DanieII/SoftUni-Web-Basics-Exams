from django.urls import path

from profiles.views import delete_profile, profile_details, create_profile

urlpatterns = [
    path('details/', profile_details, name='profile details'),
    path('delete/', delete_profile, name='delete profile'),
    path('create/', create_profile, name='create profile')
]
