from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Recipe

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class SearchForm(forms.Form):
    name = forms.CharField(required=False, max_length=100, label='Title')
    ingredient = forms.CharField(required=False, max_length=100, label='Ingredient')
    cooking_time = forms.IntegerField(required=False, label='Cooking Time')

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'cooking_time', 'instructions']