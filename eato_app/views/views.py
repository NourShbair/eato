from django.shortcuts import get_object_or_404, redirect
from ..models import Recipe
from django.contrib.auth.decorators import login_required
import random
from django.contrib import messages

 # Ensures user is logged in to access this view
@login_required
def toggle_like(request, recipe_id):
    # Get recipe or return 404 if not found
    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    # Toggle like status
    if request.user in recipe.likes.all():
        recipe.likes.remove(request.user)  # Unlike if already liked
    else:
        recipe.likes.add(request.user)     # Like if not already liked
    
    # Redirect back to previous page, or recipe_details if referrer not found
    return redirect(request.META.get('HTTP_REFERER', 'recipe_details'))

# Ensures user is logged in to access this view
@login_required  
def toggle_save(request, recipe_id):
    # Get recipe or return 404 if not found
    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    # Toggle save status
    if request.user in recipe.favorites.all():
        recipe.favorites.remove(request.user)  # Remove from favorites if already saved
    else:
        recipe.favorites.add(request.user)     # Add to favorites if not saved
    
    # Redirect back to previous page, or recipe_details if referrer not found
    return redirect(request.META.get('HTTP_REFERER', 'recipe_details'))

# Returns a random recipe from the database
def random_recipe(request):
    # Get all recipes
    recipes = Recipe.objects.all()
    
    if recipes:
        # Select a random recipe if recipes exist
        recipe = random.choice(recipes)
        return redirect('recipe_details', recipe_id=recipe.id)
    else:
        # Show warning message if no recipes available
        messages.warning(request, "No recipes available yet.")
        return redirect('home')
    
# Test view to trigger a 500 error
def crash_test(request):
    raise Exception("Test 500 error")
