from django.shortcuts import render, redirect

from fruits.forms import FruitCreateForm, FruitEditForm, FruitDeleteForm
from fruits.models import Fruit


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    context = {
        'fruits': Fruit.objects.all()
    }
    return render(request, 'dashboard.html', context)


def create_fruit(request):
    if request.method == 'POST':
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FruitCreateForm()

    context = {
        'form': form
    }
    return render(request, 'fruits/create-fruit.html', context)


def fruit_details(request, pk):
    context = {
        'fruit': Fruit.objects.get(pk=pk)
    }
    return render(request, 'fruits/details-fruit.html', context)


def edit_fruit(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    if request.method == 'POST':
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FruitEditForm(instance=fruit)

    context = {
        'fruit': fruit,
        'form': form
    }
    return render(request, 'fruits/edit-fruit.html', context)


def delete_fruit(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    if request.method == 'POST':
        fruit.delete()
        return redirect('dashboard')

    context = {
        'fruit': fruit,
        'form': FruitDeleteForm(instance=fruit)
    }
    return render(request, 'fruits/delete-fruit.html', context)
