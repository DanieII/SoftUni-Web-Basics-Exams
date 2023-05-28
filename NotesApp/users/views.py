from django.shortcuts import render, redirect

from notes.models import Note
from users.forms import ProfileForm
from users.models import Profile


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()

    return render(request, 'home/home-no-profile.html', {'form': form})


def profile_details(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile,
        'number_of_notes': Note.objects.all().count()
    }

    return render(request, 'profile/profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    profile.delete()
    Note.objects.all().delete()
    return redirect('home')
