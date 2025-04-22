from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from ...models import Recipe, AllergyTag
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

    paginator = Paginator(recipes, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'recipes/recipes_list.html', {'page_obj': page_obj})

def allergy_recipes(request, allergy_id):
    allergy = get_object_or_404(AllergyTag, id=allergy_id)

    # Get recipes that do NOT include the selected allergy
    recipes = Recipe.objects.exclude(allergies=allergy)

    paginator = Paginator(recipes, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'selected_allergy': allergy,
    }
    return render(request, 'recipes/recipe_list.html', context)