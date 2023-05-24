from django.shortcuts import render, redirect, get_object_or_404

from base.forms import RecipeForm, RecipeDeleteForm
from base.models import Recipe


def home(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context=context)


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = RecipeForm()
    context = {
        'form': form,
    }

    return render(request, 'create.html', context=context)


def edit_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = RecipeForm(instance=recipe)
    context = {
        'form': form,
    }

    return render(request, 'edit.html', context=context)


def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == 'POST':
        form = RecipeDeleteForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe.delete()
            return redirect('home')

    form = RecipeDeleteForm(instance=recipe)
    context = {
        'form': form,
    }

    return render(request, 'delete.html', context=context)


def recipe_details(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        'recipe': recipe,
    }

    return render(request, 'details.html', context=context)
