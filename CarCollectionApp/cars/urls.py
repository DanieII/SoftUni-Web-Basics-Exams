from django.urls import path, include

from cars.views import index, catalogue, create_car, car_details, edit_car, delete_car

urlpatterns = [
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue'),
    path('car/', include([
        path('create/', create_car, name='crate car'),
        path('<int:pk>/details/', car_details, name='car details'),
        path('<int:pk>/edit/', edit_car, name='edit car'),
        path('<int:pk>/delete/', delete_car, name='delete car'),
    ])),
]
