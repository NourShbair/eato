from django.test import TestCase
from django.contrib.auth.models import User
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from eato_app.models import Recipe, Ingredient, MealType, AllergyTag, Cuisine


def generate_test_image(name="test.jpg"):
    image = Image.new("RGB", (100, 100), color="red")
    buffer = BytesIO()
    image.save(buffer, format="JPEG")
    buffer.seek(0)
    return SimpleUploadedFile(name, buffer.read(), content_type="image/jpeg")


class EatoCoreTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='chef', password='test123')   # noqa
        self.client.login(username='chef', password='test123')

        self.cuisine = Cuisine.objects.create(name='Italian')
        self.meal_type = MealType.objects.create(name='Dinner')
        self.allergy_tag = AllergyTag.objects.create(name='Gluten')
        self.image = generate_test_image()

    def test_create_recipe_with_ingredients(self):
        recipe = Recipe.objects.create(
            title="Carbonara",
            description="Creamy pasta with pancetta",
            instructions="1. Boil pasta\n2. Cook pancetta\n3. Mix with eggs and cheese",   # noqa
            image=self.image,
            cuisine=self.cuisine,
            created_by=self.user,
        )
        recipe.meal_types.add(self.meal_type)
        recipe.allergy_tags.add(self.allergy_tag)

        spaghetti = Ingredient.objects.create(name="Spaghetti")
        eggs = Ingredient.objects.create(name="Eggs")

        from eato_app.models import RecipeIngredient

        RecipeIngredient.objects.create(recipe=recipe, ingredient=spaghetti, quantity=200, unit="g")   # noqa
        RecipeIngredient.objects.create(recipe=recipe, ingredient=eggs, quantity=2, unit="pcs")   # noqa

        self.assertEqual(Recipe.objects.count(), 1)
        self.assertEqual(recipe.ingredients.count(), 2)
        self.assertIn(self.meal_type, recipe.meal_types.all())
        self.assertIn(self.allergy_tag, recipe.allergy_tags.all())

    def test_like_and_favorite_recipe(self):
        recipe = Recipe.objects.create(
            title="Margherita Pizza",
            description="Classic cheese and tomato pizza",
            instructions="Bake it",
            image=self.image,
            cuisine=self.cuisine,
            created_by=self.user,
        )
        recipe.likes.add(self.user)
        recipe.favorites.add(self.user)

        self.assertEqual(recipe.total_likes(), 1)
        self.assertEqual(recipe.total_favorites(), 1)

    def test_user_profile_recipe_listing(self):
        Recipe.objects.create(
            title="Pesto Pasta",
            description="Basil pesto with pine nuts",
            instructions="Mix and serve",
            image=self.image,
            cuisine=self.cuisine,
            created_by=self.user,
        )
        response = self.client.get(f'/recipes/?filter={self.user.username}/')
        self.assertContains(response, "Pesto Pasta")

    def test_search_recipe_by_title(self):
        Recipe.objects.create(
            title="Tomato Soup",
            description="Simple tomato-based soup",
            instructions="Blend and simmer",
            image=self.image,
            cuisine=self.cuisine,
            created_by=self.user,
        )
        response = self.client.get('/search/?q=tomato')
        self.assertContains(response, "Tomato Soup")
