from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Ingredient
from recipes.models import Recipe
from .forms import IngredientForm

@login_required
def add_ingredient(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()
            return redirect('recipes:recipe_detail', id=recipe.id)
    else:
        form = IngredientForm()
    return render(request, 'ingredients/add_ingredient.html', {'form': form, 'recipe': recipe})

@login_required
def edit_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('recipes:recipe_detail', id=ingredient.recipe.id)
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 'ingredients/edit_ingredient.html', {'form': form, 'recipe': ingredient.recipe})

@login_required
def delete_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, id=ingredient_id)
    recipe_id = ingredient.recipe.id
    if request.method == 'POST':
        ingredient.delete()
        return redirect('recipes:recipe_detail', id=recipe_id)
    return render(request, 'ingredients/delete_ingredient.html', {'ingredient': ingredient})
