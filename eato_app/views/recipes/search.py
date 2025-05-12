from django.shortcuts import render
from ...models import Recipe, MealType, Cuisine
from django.core.paginator import Paginator
from django.db.models import Q


def recipe_search(request):
    # Get search parameters from URL query string
    query = request.GET.get('q', '')  # Search text query
    category_id = request.GET.get('category')  # Meal type filter
    cuisine_id = request.GET.get('cuisine')  # Cuisine filter

    # Start with all recipes
    recipes = Recipe.objects.all()

    # Apply text search filter if query exists
    if query:
        # Search in multiple fields using Q objects for OR conditions
        recipes = recipes.filter(
            Q(title__icontains=query) |  # Search in recipe title
            Q(recipeingredient__ingredient__name__icontains=query) |  # Search in ingredients   # noqa
            Q(instructions__icontains=query)  # Search in instructions
        )

    # Filter by meal type if category is selected
    if category_id:
        recipes = recipes.filter(meal_types__id=category_id)

    # Filter by cuisine if cuisine is selected
    if cuisine_id:
        recipes = recipes.filter(cuisine__id=cuisine_id)

    # Remove duplicates that might occur from OR conditions
    recipes = recipes.distinct()

    # Set up pagination
    paginator = Paginator(recipes, 6)  # Show 6 recipes per page
    page_number = request.GET.get('page')  # Get requested page number
    page_obj = paginator.get_page(page_number)  # Get Page object

    # Prepare context data for template
    context = {
        'query': query,  # Current search query
        'page_obj': page_obj,  # Paginated results
        'meal_types': MealType.objects.all(),  # All meal types for filter options   # noqa
        'cuisines': Cuisine.objects.all(),  # All cuisines for filter options
        'selected_category': category_id,  # Currently selected category
        'selected_cuisine': cuisine_id,  # Currently selected cuisine
    }

    # Render search results template with context
    return render(request, 'recipes/search_results.html', context)
