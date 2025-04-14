from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import Recipe
from .add_recipe import RecipeForm


def recipe_details(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingredients = recipe.recipeingredient_set.all()

    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(request, 'recipes/recipe_details.html', context)

@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, created_by=request.user)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, "Recipe updated successfully!")
            return redirect('recipe_details', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'recipes/edit_recipe.html', {'form': form, 'recipe': recipe})

@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, created_by=request.user)

    if request.method == 'POST':
        recipe.delete()
        messages.success(request, "Recipe deleted.")
        return redirect('recipe_list')

    return render(request, 'recipes/delete_recipe.html', {'recipe': recipe})