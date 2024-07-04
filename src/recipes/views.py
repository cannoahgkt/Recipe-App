from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Recipe
from .forms import SignUpForm, SearchForm, RecipeForm

def home_view(request):
    return render(request, 'recipes/recipes_home.html')

@login_required
def recipes_list(request):
    form = SearchForm(request.GET)
    recipes = Recipe.objects.all().distinct()  # Ensure distinct recipes
    
    if form.is_valid():
        name = form.cleaned_data.get('name')
        ingredient = form.cleaned_data.get('ingredient')
        cooking_time = form.cleaned_data.get('cooking_time')
        
        if name:
            recipes = recipes.filter(name__icontains=name)
        if ingredient:
            recipes = recipes.filter(ingredients__name__icontains=ingredient)  # Corrected lookup
        if cooking_time:
            recipes = recipes.filter(cooking_time=cooking_time)

    return render(request, 'recipes/recipes_list.html', {
        'form': form,
        'recipes': recipes  # Directly pass the queryset to the template
    })

@login_required
def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    ingredients = recipe.ingredients.all()
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe, 'ingredients': ingredients})

def logout_view(request):
    logout(request)
    return redirect('recipes:logout_success')

def logout_success_view(request):
    return render(request, 'recipes/logout_success.html')

def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipes:home')
    else:
        form = SignUpForm()
    return render(request, 'recipes/register.html', {'form': form})

class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipes:recipe_list')

class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipes:recipe_list')

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipes:recipe_list')
