from django.urls import path
from . import views
from ingredients.views import add_ingredient, edit_ingredient, delete_ingredient

app_name = 'recipes'

urlpatterns = [
    path('', views.recipes_list, name='recipes_list'),
    path('<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('add/', views.RecipeCreateView.as_view(), name='recipe_add'),
    path('<int:pk>/edit/', views.RecipeUpdateView.as_view(), name='recipe_edit'),
    path('<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),
    path('<int:recipe_id>/add_ingredient/', add_ingredient, name='add_ingredient'),
    path('ingredient/<int:ingredient_id>/edit/', edit_ingredient, name='edit_ingredient'),
    path('ingredient/<int:ingredient_id>/delete/', delete_ingredient, name='delete_ingredient'),
    path('register/', views.register_view, name='register'),
]
