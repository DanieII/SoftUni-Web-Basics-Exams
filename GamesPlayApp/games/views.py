from django.shortcuts import render, redirect

from games.forms import GameForm, DeleteGameForm
from games.models import Game
from profiles.models import Profile


def get_profile():
    return Profile.objects.first()


def home(request):
    context = {
        'profile': get_profile(),
    }
    return render(request, 'home/home-page.html', context)


def dashboard(request):
    context = {
        'games': Game.objects.all(),
        'profile': get_profile(),
    }
    return render(request, 'dashboard/dashboard.html', context)


def create_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = GameForm()

    context = {
        'form': form,
        'profile': get_profile(),
    }
    return render(request, 'game/create-game.html', context)


def game_details(request, pk):
    game = Game.objects.get(pk=pk)
    context = {
        'game': game,
        'profile': get_profile(),
    }
    return render(request, 'game/details-game.html', context)


def edit_game(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = GameForm(instance=game)

    context = {
        'form': form,
        'profile': get_profile(),
    }
    return render(request, 'game/edit-game.html', context)


def delete_game(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            game.delete()
            return redirect('dashboard')
    else:
        form = DeleteGameForm(instance=game)

    context = {
        'form': form,
        'profile': get_profile(),
    }
    return render(request, 'game/delete-game.html', context)
