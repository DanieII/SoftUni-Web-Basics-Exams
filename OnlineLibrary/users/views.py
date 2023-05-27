from django.shortcuts import render, redirect

from users.forms import ProfileForm
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
