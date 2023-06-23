from django.shortcuts import render, redirect

from albums.models import Album
from profiles.forms import ProfileForm
from profiles.models import Profile


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()

    context = {
        'form': form
    }
    return render(request, 'home/home-no-profile.html', context)


def profile_details(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile,
        'number_of_albums': Album.objects.all().count(),
    }
    return render(request, 'profile/profile-details.html', context)


def delete_profile(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        profile.delete()
        Album.objects.all().delete()
        return redirect('home')
    return render(request, 'profile/profile-delete.html')
