from django.db import models
from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

# Cuisine model (e.g., Italian, Middle Eastern, etc.)
class Cuisine(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# MealType model (e.g., Breakfast, Lunch, Dinner)
class MealType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# AllergyTag model (e.g., Gluten-Free, Dairy-Free)
class AllergyTag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Ingredient model (e.g., Flour, Eggs, Milk)
class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Recipe model (Main model for storing recipes)
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # User who created the recipe
    cuisine = models.ForeignKey(Cuisine, on_delete=models.SET_NULL, null=True)
    image = CloudinaryField('image', null=True, blank=True)  # Store images on Cloudinary
    likes = models.ManyToManyField(User, related_name='liked_recipes', blank=True)
    favorites = models.ManyToManyField(User, related_name='favorite_recipes', blank=True)
    
    # Many-to-Many relationships
    meal_types = models.ManyToManyField(MealType, blank=True)
    allergy_tags = models.ManyToManyField(AllergyTag, blank=True)

    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()

    def total_favorites(self):
        return self.favorites.count()

# RecipeIngredient model (Intermediate model to store ingredient details)
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)  # Example: 'grams', 'cups'

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.ingredient.name} in {self.recipe.title}"

# Likes model (Tracks users who liked a recipe)
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')  # Prevent duplicate likes

    def __str__(self):
        return f"{self.user.username} likes {self.recipe.title}"

# Favorites model (Tracks saved recipes)
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')  # Prevent duplicate saves

    def __str__(self):
        return f"{self.user.username} saved {self.recipe.title}"