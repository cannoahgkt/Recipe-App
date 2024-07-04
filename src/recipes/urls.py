from django.urls import path
from . import views
from ingredients.views import add_ingredient, edit_ingredient, delete_ingredient

app_name = 'recipes'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('list/', views.recipes_list, name='recipe_list'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/add/', views.RecipeCreateView.as_view(), name='recipe_add'),
    path('recipe/<int:pk>/edit/', views.RecipeUpdateView.as_view(), name='recipe_edit'),
    path('recipe/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),
    path('recipe/<int:recipe_id>/add_ingredient/', add_ingredient, name='add_ingredient'),
    path('ingredient/<int:ingredient_id>/edit/', edit_ingredient, name='edit_ingredient'),
    path('ingredient/<int:ingredient_id>/delete/', delete_ingredient, name='delete_ingredient'),
    path('logout/', views.logout_view, name='logout'),
    path('logout/success/', views.logout_success_view, name='logout_success'),
    path('register/', views.register_view, name='register'),
]
