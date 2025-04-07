from ..models import Recipe, MealType, Cuisine
from django.db.models import Q
from django.shortcuts import render

def recipe_search(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category')
    cuisine_id = request.GET.get('cuisine')

    recipes = Recipe.objects.all()

    if query:
        recipes = recipes.filter(
            Q(title__icontains=query) |
            Q(ingredients__icontains=query) |
            Q(instructions__icontains=query)
        )

    if category_id:
        recipes = recipes.filter(meal_types__id=category_id)

    if cuisine_id:
        recipes = recipes.filter(cuisine__id=cuisine_id)

    context = {
        'query': query,
        'results': recipes.distinct(),
        'meal_types': MealType.objects.all(),
        'cuisines': Cuisine.objects.all(),
    }

    return render(request, 'search_results.html', context)