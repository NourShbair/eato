from django.shortcuts import render, get_object_or_404
from ..models import Recipe

def recipe_details(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingredients = recipe.recipeingredient_set.all()

    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(request, 'recipe_details.html', context)