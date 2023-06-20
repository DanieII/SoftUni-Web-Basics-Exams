from django.shortcuts import render, redirect

from plants.forms import PlantForm, DeletePlantForm
from plants.models import Plant
from profiles.models import Profile
from profiles.views import create_profile


def home(request):
    profile = Profile.objects.first()

    if not profile:
        return create_profile(request)

    context = {
        'profile': profile
    }
    return render(request, 'home-page.html', context)


def catalogue(request):
    profile = Profile.objects.first()
    plants = Plant.objects.all()

    context = {
        'profile': profile,
        'plants': plants
    }
    return render(request, 'catalogue.html', context)


def create_plant(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = PlantForm()

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'plants/create-plant.html', context)


def plant_details(request, pk):
    profile = Profile.objects.first()
    plant = Plant.objects.get(pk=pk)

    context = {
        'profile': profile,
        'plant': plant
    }
    return render(request, 'plants/plant-details.html', context)


def edit_plant(request, pk):
    profile = Profile.objects.first()
    plant = Plant.objects.get(pk=pk)

    if request.method == 'POST':
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = PlantForm(instance=plant)

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'plants/edit-plant.html', context)


def delete_plant(request, pk):
    profile = Profile.objects.first()
    plant = Plant.objects.get(pk=pk)

    if request.method == 'POST':
        plant.delete()
        return redirect('catalogue')

    context = {
        'profile': profile,
        'form': DeletePlantForm(instance=plant)
    }
    return render(request, 'plants/delete-plant.html', context)
