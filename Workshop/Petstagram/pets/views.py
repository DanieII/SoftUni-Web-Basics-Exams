from django.shortcuts import render

from pets.models import Pet


def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()

    context = {
        'pet': pet,
        'all_photos': all_photos
    }
    return render(request, 'pets/pet-details-page.html', context)
