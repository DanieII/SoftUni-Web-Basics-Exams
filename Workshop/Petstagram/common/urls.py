from django.urls import path

from common.views import home, like, share, comment, search_by_pet_name

urlpatterns = [
    path('', home, name='home'),
    path('like/<int:photo_id>/', like, name='like'),
    path('share/<int:photo_id>/', share, name='share'),
    path('comment/<int:photo_id>/', comment, name='comment'),
    path('search/', search_by_pet_name, name='search by pet name'),
]
