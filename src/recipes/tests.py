from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from recipes.models import Recipe
from ingredients.models import Ingredient

class RecipeViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.recipe = Recipe.objects.create(
            name='Test Recipe',
            description='Test Description',
            cooking_time=10,
            instructions='Test Instructions'
        )
        self.ingredient = Ingredient.objects.create(
            name='Test Ingredient',
            quantity=1,
            unit='unit',
            recipe=self.recipe
        )

    def test_login_required_redirect(self):
        response = self.client.get(reverse('recipes:recipe_list'))
        self.assertRedirects(response, f'/accounts/login/?next=/list/')

    def test_recipe_create_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('recipes:recipe_add'), {
            'name': 'New Recipe',
            'description': 'New Description',
            'cooking_time': 15,
            'instructions': 'New Instructions'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Recipe.objects.count(), 2)

    def test_recipe_delete_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('recipes:recipe_delete', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Recipe.objects.count(), 0)

    def test_recipe_update_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('recipes:recipe_edit', args=[self.recipe.id]), {
            'name': 'Updated Recipe',
            'description': 'Updated Description',
            'cooking_time': 20,
            'instructions': 'Updated Instructions'
        })
        self.assertEqual(response.status_code, 302)
        self.recipe.refresh_from_db()
        self.assertEqual(self.recipe.name, 'Updated Recipe')

    def test_recipes_list_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('recipes:recipe_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Recipe')

    def test_recipe_detail_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('recipes:recipe_detail', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Recipe')
        self.assertContains(response, 'Test Ingredient')
