from django.shortcuts import render
from django.core.paginator import Paginator
from ..models import Recipe
from django.contrib.auth.decorators import login_required

# @login_required
def recipes_list(request):
    filter_by = request.GET.get('filter')
    recipes = Recipe.objects.all()

    if filter_by == 'mine':
        recipes = recipes.filter(created_by=request.user)
    elif filter_by == 'liked':
        recipes = request.user.liked_recipes.all()
    elif filter_by == 'saved':
        recipes = request.user.favorite_recipes.all()

    paginator = Paginator(recipes, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'recipes/recipes_list.html', {'page_obj': page_obj})