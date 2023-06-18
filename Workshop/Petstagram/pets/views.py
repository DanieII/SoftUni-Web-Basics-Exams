from django.shortcuts import render, redirect

from common.forms import CommentForm
from pets.forms import PetForm, PetDeleteForm
from pets.models import Pet


def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()

    context = {
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': CommentForm()
    }
    return render(request, 'pets/pet-details-page.html', context)


def add_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = PetForm

    context = {
        'form': form,
    }
    return render(request, 'pets/pet-add-page.html', context)


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet details', username=username, pet_slug=pet_slug)
    else:
        form = PetForm(instance=pet)

    context = {
        'form': form,
        'pet': pet
    }
    return render(request, 'pets/pet-edit-page.html', context)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'POST':
        pet.delete()
        return redirect('profile details', pk=1)

    context = {
        'form': PetDeleteForm(instance=pet)

    }
    return render(request, 'pets/pet-delete-page.html', context)