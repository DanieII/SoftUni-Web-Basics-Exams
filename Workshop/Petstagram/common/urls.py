from django.urls import path

from common.views import home, like, share

urlpatterns = [
    path('', home, name='home'),
    path('/like/<int:photo_id>/', like, name='like'),
    path('/share/<int:photo_id>/', share, name='share'),
]
