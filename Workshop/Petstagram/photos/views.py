from django.shortcuts import render, redirect

from photos.forms import PhotoForm, EditPhotoForm
from photos.models import Photo


def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.count()
    comments = photo.comment_set.all()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments
    }
    return render(request, 'photos/photo-details-page.html', context)


def add_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PhotoForm()

    context = {
        'form': form
    }
    return render(request, 'photos/photo-add-page.html', context)


def edit_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditPhotoForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo details', pk=pk)
    else:
        form = EditPhotoForm(instance=photo)

    context = {
        'form': form
    }
    return render(request, 'photos/photo-edit-page.html', context)


def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('home')
