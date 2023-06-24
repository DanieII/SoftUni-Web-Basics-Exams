from django.shortcuts import render, redirect

from fruits.models import Fruit
from profiles.forms import ProfileCreateForm, ProfileEditForm
from profiles.models import Profile


def create_profile(request):
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProfileCreateForm()

    context = {
        'form': form
    }
    return render(request, 'profiles/create-profile.html', context)


def profile_details(request):
    context = {
        'number_of_posts': Fruit.objects.all().count()
    }
    return render(request, 'profiles/details-profile.html', context)


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
        Fruit.objects.all().delete()
        return redirect('index')

    return render(request, 'profiles/delete-profile.html')
