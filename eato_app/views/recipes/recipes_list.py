from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from ...models import Recipe, AllergyTag
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def recipes_list(request):
    # Get filter parameter from URL query string
    filter_by = request.GET.get('filter')
    # Initially get all recipes
    recipes = Recipe.objects.all()

    # Apply filters based on URL parameter
    if filter_by == 'mine':
        # Show only recipes created by current user
        recipes = recipes.filter(created_by=request.user)
    elif filter_by == 'liked':
        # Show recipes liked by current user
        recipes = request.user.liked_recipes.all()
    elif filter_by == 'saved':
        # Show recipes saved/favorited by current user
        recipes = request.user.favorite_recipes.all()

    # Set up pagination
    paginator = Paginator(recipes, 6)  # Show 6 recipes per page
    # Get the requested page number from URL
    page_number = request.GET.get('page')
    # Get the Page object for the requested page
    page_obj = paginator.get_page(page_number)

    # Render the template with paginated recipes
    return render(request, 'recipes/recipes_list.html', {
        'page_obj': page_obj
    })

# View function to display recipes filtered by allergy
def allergy_recipes(request, allergy_id):
    # Get the allergy object or return 404 if not found
    allergy = get_object_or_404(AllergyTag, id=allergy_id)
    
    # Get all recipes that don't have this allergy tag
    # distinct() ensures no duplicate recipes
    recipes = Recipe.objects.exclude(allergy_tags=allergy).distinct()
    
    # Set up pagination
    paginator = Paginator(recipes, 6)  # Show 6 recipes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Render template with filtered recipes
    return render(request, 'recipes/recipes_list.html', {
        'recipes': recipes,
        'filter_type': f"Allergy: {allergy.name}",  # Display current filter
        'page_obj': page_obj,
        'selected_allergy': allergy,  # Pass selected allergy for UI highlighting
    })
