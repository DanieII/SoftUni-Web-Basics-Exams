from django.shortcuts import render, redirect

from games.models import Game
from profiles.forms import CreateProfileForm, EditProfileForm
from profiles.models import Profile


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    profile = Profile.objects.first()

    if profile.first_name and profile.last_name:
        name = profile.first_name + " " + profile.last_name
    elif not profile.first_name and profile.last_name:
        name = profile.last_name
    elif not profile.last_name and profile.first_name:
        name = profile.first_name
    else:
        name = None

    all_games = Game.objects.all()
    total_number_of_games = all_games.count()
    context = {
        'profile': profile,
        'name': name,
        'total_number_of_games': total_number_of_games,
        'average_rating_of_games': sum(
            [x.rating for x in all_games]) / total_number_of_games if total_number_of_games else "0.0",
    }
    return render(request, 'profile/details-profile.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditProfileForm(instance=profile)
        # If the password needs to be filled when editing
        form.fields['password'].widget.attrs['value'] = profile.password

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        profile.delete()
        Game.objects.all().delete()
        return redirect('home')

    context = {
        'profile': profile,
    }
    return render(request, 'profile/delete-profile.html', context)
