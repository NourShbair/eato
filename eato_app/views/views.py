
from django.shortcuts import get_object_or_404, redirect
from ..models import Recipe
from django.contrib.auth.decorators import login_required

@login_required
def toggle_like(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user in recipe.likes.all():
        recipe.likes.remove(request.user)
    else:
        recipe.likes.add(request.user)
    return redirect(request.META.get('HTTP_REFERER', 'recipe_detail'))

@login_required
def toggle_save(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.user in recipe.favorites.all():
        recipe.favorites.remove(request.user)
    else:
        recipe.favorites.add(request.user)
    return redirect(request.META.get('HTTP_REFERER', 'recipe_detail'))
