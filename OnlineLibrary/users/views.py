from django.shortcuts import render, redirect, get_object_or_404

from books.models import Book
from users.forms import ProfileForm, DeleteProfileForm
from users.models import Profile


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            Profile.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = ProfileForm()

    context = {
        'form': form,
        'profile': None,
    }
    return render(request, 'home-no-profile.html', context)


def profile_details(request):
    context = {
        'profile': Profile.objects.first(),
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile.delete()
            Book.objects.all().delete()
            return redirect('home')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'delete-profile.html', context)
