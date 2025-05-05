from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from ..models import Recipe, MealType, Cuisine, AllergyTag
import random

# Main home view function
def home(request):
    # Get current user
    user = request.user
    
    # Fetch all required data from database
    meal_types = MealType.objects.all()
    cuisines = Cuisine.objects.all().order_by('name')  # Sort cuisines alphabetically
    allergies = AllergyTag.objects.all()
    # Get 5 most recent recipes
    recent_recipes = Recipe.objects.order_by('-created_at')[:5]

    # Handle random recipe feature
    random_recipe = None
    recipes = Recipe.objects.all()
    # If random=1 is in URL parameters and recipes exist, select a random recipe
    if request.GET.get("random") == "1" and recipes.exists():
        random_recipe = random.choice(recipes)

    # Initialize user-specific counters
    user_recipe_count = 0
    user_liked_count = 0
    user_saved_count = 0
    
    # If user is logged in, get their statistics
    if user.is_authenticated:
        # Count recipes created by user
        user_recipe_count = Recipe.objects.filter(created_by=user).count()
        # Count recipes liked by user
        user_liked_count = Recipe.objects.filter(likes=user).count()
        # Count recipes saved by user
        user_saved_count = Recipe.objects.filter(favorites=user).count()

    # Prepare context data for template
    context = {
        'meal_types': meal_types,
        'cuisines': cuisines,
        'allergies': allergies,
        'recent_recipes': recent_recipes,
        'user_recipe_count': user_recipe_count,
        'user_liked_count': user_liked_count,
        'user_saved_count': user_saved_count,
        'random_recipe': random_recipe,
        'has_recipes': recipes.exists(),
    }

    # Render the home page with context data
    return render(request, 'index.html', context)

# View function to display recipes by meal type
def meal_type_recipes(request, meal_type_id):
    # Filter recipes by meal type ID
    recipes = Recipe.objects.filter(meal_types__id=meal_type_id)
    return render(request, 'recipes_list.html', {'recipes': recipes})

# View function to display recipes by cuisine
def cuisine_recipes(request, cuisine_id):
    # Get cuisine object or return 404 if not found
    cuisine = get_object_or_404(Cuisine, id=cuisine_id)
    # Filter recipes by cuisine
    recipes = Recipe.objects.filter(cuisine=cuisine)
    return render(request, 'recipes_list.html', {
        'recipes': recipes,
        'filter_type': f"Cuisine: {cuisine.name}"  # Add filter type for display
    })

# View function to display recipes excluding specific allergy
def allergy_recipes(request, allergy_id):
    # Get allergy object or return 404 if not found
    allergy = get_object_or_404(AllergyTag, id=allergy_id)
    # Get recipes that don't have this allergy tag
    recipes = Recipe.objects.exclude(allergy_tags=allergy).distinct()
    
    # Set up pagination (6 recipes per page)
    paginator = Paginator(recipes, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'recipes/recipes_list.html', {
        'recipes': recipes,
        'filter_type': f"Allergy: {allergy.name}",
        'page_obj': page_obj,
        'selected_allergy': allergy,
    })

# View function to display user's liked recipes
# Requires user to be logged in
@login_required
def my_likes(request):
    # Get all recipes liked by the current user
    recipes = request.user.liked_recipes.all()
    return render(request, 'my_likes.html', {'recipes': recipes})

# View function to display user's saved recipes
# Requires user to be logged in
@login_required
def my_saves(request):
    # Get all recipes saved by the current user
    recipes = request.user.favorite_recipes.all()
    return render(request, 'my_saves.html', {'recipes': recipes})
