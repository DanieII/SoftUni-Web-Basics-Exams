from django.shortcuts import render, redirect

from albums.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from albums.models import Album
from profiles.models import Profile
from profiles.views import create_profile


def home(request):
    profile = Profile.objects.first()
    if not profile:
        return create_profile(request)

    context = {
        'albums': Album.objects.all()
    }
    return render(request, 'home-with-profile.html', context)


def add_album(request):
    if request.method == 'POST':
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlbumCreateForm()

    context = {
        'form': form
    }
    return render(request, 'albums/add-album.html', context)


def album_details(request, id):
    context = {
        'album': Album.objects.get(id=id)
    }
    return render(request, 'albums/album-details.html', context)


def edit_album(request, id):
    album = Album.objects.get(id=id)
    if request.method == 'POST':
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlbumEditForm(instance=album)

    context = {
        'album': album,
        'form': form
    }
    return render(request, 'albums/edit-album.html', context)


def delete_album(request, id):
    album = Album.objects.get(id=id)
    if request.method == 'POST':
        album.delete()
        return redirect('home')
    else:
        form = AlbumDeleteForm(instance=album)

    context = {
        'album': album,
        'form': form
    }
    return render(request, 'albums/delete-album.html', context)
