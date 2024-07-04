from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from recipes.models import Recipe
from .models import Ingredient

class IngredientTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.recipe = Recipe.objects.create(name='Test Recipe', description='Test Description', cooking_time=10, instructions='Test Instructions')
        self.ingredient = Ingredient.objects.create(name='Test Ingredient', quantity=1, unit='unit', recipe=self.recipe)

    def test_add_ingredient_to_recipe(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('recipes:add_ingredient', args=[self.recipe.id]), {
            'name': 'New Ingredient',
            'quantity': 2,
            'unit': 'unit'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Ingredient.objects.count(), 2)

    def test_delete_ingredient(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('recipes:delete_ingredient', args=[self.ingredient.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Ingredient.objects.count(), 0)

    def test_update_ingredient(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('recipes:edit_ingredient', args=[self.ingredient.id]), {
            'name': 'Updated Ingredient',
            'quantity': 2,
            'unit': 'unit'
        })
        self.assertEqual(response.status_code, 302)
        self.ingredient.refresh_from_db()
        self.assertEqual(self.ingredient.name, 'Updated Ingredient')

    def test_ingredient_in_recipe_detail(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('recipes:recipe_detail', args=[self.recipe.id]))
        self.assertContains(response, 'Test Ingredient')

    def test_ingredient_str_method(self):
        self.assertEqual(str(self.ingredient), '1 unit of Test Ingredient')
