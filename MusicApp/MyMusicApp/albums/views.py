from django.shortcuts import render, redirect

from albums.forms import AlbumForm, DeleteAlbumForm
from albums.models import Album
from profiles.models import Profile
from profiles.views import create_profile


def home(request):
    profile = Profile.objects.first()
    if not profile:
        return create_profile(request)

    context = {
        'profile': profile,
        'albums': Album.objects.all(),
    }
    return render(request, 'home/home-with-profile.html', context)


def add_album(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlbumForm()

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'albums/add-album.html', context)


def album_details(request, pk):
    profile = Profile.objects.first()
    album = Album.objects.get(id=pk)

    context = {
        'album': album,
        'profile': profile,
    }
    return render(request, 'albums/album-details.html', context)


def edit_album(request, pk):
    profile = Profile.objects.first()
    album = Album.objects.get(id=pk)

    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlbumForm(instance=album)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'albums/edit-album.html', context)


def delete_album(request, pk):
    profile = Profile.objects.first()
    album = Album.objects.get(id=pk)

    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            album.delete()
            return redirect('home')
    else:
        form = DeleteAlbumForm(instance=album)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'albums/delete-album.html', context)
