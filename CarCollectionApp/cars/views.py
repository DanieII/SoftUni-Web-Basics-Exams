from django.shortcuts import render, redirect

from cars.forms import CarForm, DeleteCarForm
from cars.models import Car
from profiles.models import Profile


def get_profile():
    return Profile.objects.first()


def index(request):
    context = {
        'profile': get_profile()
    }
    return render(request, 'index.html', context)


def catalogue(request):
    context = {
        'profile': get_profile(),
        'cars': Car.objects.all(),
    }
    return render(request, 'catalogue.html', context)


def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarForm()

    context = {
        'profile': get_profile(),
        'form': form,
    }
    return render(request, 'cars/car-create.html', context)


def car_details(request, pk):
    context = {
        'profile': get_profile(),
        'car': Car.objects.get(pk=pk)
    }
    return render(request, 'cars/car-details.html', context)


def edit_car(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarForm(instance=car)

    context = {
        'profile': get_profile(),
        'form': form,
    }
    return render(request, 'cars/car-edit.html', context)


def delete_car(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')
    form = DeleteCarForm(instance=car)

    context = {
        'profile': get_profile(),
        'form': form,
    }
    return render(request, 'cars/car-delete.html', context)
