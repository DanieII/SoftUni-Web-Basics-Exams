from django.shortcuts import render, redirect

from plants.models import Plant
from profiles.forms import CreateProfileForm, EditProfileForm
from profiles.models import Profile


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CreateProfileForm()

    context = {
        'form': form
    }
    return render(request, 'profiles/create-profile.html', context)


def profile_details(request):
    context = {
        'profile': Profile.objects.first(),
        'number_of_stars': Plant.objects.all().count()
    }
    return render(request, 'profiles/profile-details.html', context)


def edit_profile(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'profile': profile,
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
