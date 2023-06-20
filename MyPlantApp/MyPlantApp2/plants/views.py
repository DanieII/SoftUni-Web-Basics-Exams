from django.shortcuts import render, redirect

from plants.forms import CreatePlantForm, EditPlantForm, DeletePlantForm
from plants.models import Plant


def home(request):
    return render(request, 'home-page.html')


def catalogue(request):
    context = {
        'plants': Plant.objects.all()
    }
    return render(request, 'catalogue.html', context)


def create_plant(request):
    if request.method == 'POST':
        form = CreatePlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CreatePlantForm()

    context = {
        'form': form
    }
    return render(request, 'plants/create-plant.html', context)


def plant_details(request, plant_id):
    context = {
        'plant': Plant.objects.get(id=plant_id)
    }
    return render(request, 'plants/plant-details.html', context)


def edit_plant(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    if request.method == 'POST':
        form = EditPlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = EditPlantForm(instance=plant)

    context = {
        'form': form,
        'plant': plant
    }
    return render(request, 'plants/edit-plant.html', context)


def delete_plant(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    if request.method == 'POST':
        plant.delete()
        return redirect('catalogue')

    context = {
        'form': DeletePlantForm(instance=plant),
        'plant': plant
    }
    return render(request, 'plants/delete-plant.html', context)
