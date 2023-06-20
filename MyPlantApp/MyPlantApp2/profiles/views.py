from django.shortcuts import render, redirect

from plants.models import Plant
from .forms import ProfileCreateForm, ProfileEditForm
from .models import Profile


def create_profile(request):
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProfileCreateForm()

    context = {
        'form': form
    }
    return render(request, 'profiles/create-profile.html', context)


def profile_details(request):
    context = {
        'stars': Plant.objects.all()[:3]
    }
    return render(request, 'profiles/profile-details.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileEditForm(instance=profile)

    context = {
        'form': form
    }
    return render(request, 'profiles/edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        profile.delete()
        Plant.objects.all().delete()
        return redirect('home')

    return render(request, 'profiles/delete-profile.html')
