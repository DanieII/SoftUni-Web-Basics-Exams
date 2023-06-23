from django.shortcuts import render, redirect

from albums.models import Album
from profiles.forms import ProfileCreateForm
from profiles.models import Profile


def profile_details(request):
    context = {
        'number_of_albums': Album.objects.all().count()
    }
    return render(request, 'profiles/profile-details.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        profile.delete()
        Album.objects.all().delete()
        return redirect('home')

    return render(request, 'profiles/profile-delete.html')


def create_profile(request):
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileCreateForm()

    context = {
        'form': form
    }
    return render(request, 'home-no-profile.html', context)
