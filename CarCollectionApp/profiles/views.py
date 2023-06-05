from django.shortcuts import render, redirect

from cars.models import Car
from profiles.forms import ProfileForm, EditProfileForm
from profiles.models import Profile


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProfileForm()

    context = {
        'form': form
    }
    return render(request, 'profiles/profile-create.html', context)


def profile_details(request):
    profile = Profile.objects.first()
    cars = Car.objects.all()
    total_cars_price = sum([x.price for x in cars])

    if profile.first_name and profile.last_name:
        name = profile.first_name + profile.last_name
    elif profile.first_name and not profile.last_name:
        name = profile.first_name
    elif profile.last_name and not profile.first_name:
        name = profile.last_name
    else:
        name = None

    context = {
        'profile': profile,
        'name': name,
        'cars': cars,
        'total_cars_price': total_cars_price,
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
        form.fields['password'].widget.attrs['value'] = profile.password

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profiles/profile-edit.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        profile.delete()
        Car.objects.all().delete()
        return redirect('index')

    context = {
        'profile': profile,
    }
    return render(request, 'profiles/profile-delete.html', context)
