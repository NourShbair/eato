from django.shortcuts import render
from ...models import Recipe, MealType, Cuisine
from django.core.paginator import Paginator
from django.db.models import Q

def recipe_search(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category')
    cuisine_id = request.GET.get('cuisine')

    recipes = Recipe.objects.all()

    if query:
        recipes = recipes.filter(
            Q(title__icontains=query) |
            Q(recipeingredient__ingredient__name__icontains=query) |
            Q(instructions__icontains=query)
        )

    if category_id:
        recipes = recipes.filter(meal_types__id=category_id)

    if cuisine_id:
        recipes = recipes.filter(cuisine__id=cuisine_id)

    recipes = recipes.distinct()

    # Pagination
    paginator = Paginator(recipes, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'query': query,
        'page_obj': page_obj,
        'meal_types': MealType.objects.all(),
        'cuisines': Cuisine.objects.all(),
        'selected_category': category_id,
        'selected_cuisine': cuisine_id,
    }

    return render(request, 'recipes/search_results.html', context)