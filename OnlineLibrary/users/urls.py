from django.urls import path, include

from users.views import create_profile

urlpatterns = [
    path('create', create_profile, name='create profile')
]
