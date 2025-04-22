from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Recipe, MealType, Cuisine, AllergyTag
import random

# @login_required
def home(request):
    user = request.user
    meal_types = MealType.objects.all()
    cuisines = Cuisine.objects.all()
    allergies = AllergyTag.objects.all()
    recent_recipes = Recipe.objects.order_by('-created_at')[:5]  # Latest 5 recipes



    random_recipe = None
    recipes = Recipe.objects.all()
    if request.GET.get("random") == "1" and recipes.exists():
        random_recipe = random.choice(recipes)

    user_recipe_count = 0
    user_liked_count = 0
    user_saved_count = 0
    
    if user.is_authenticated:
        user_recipe_count = Recipe.objects.filter(created_by=user).count()
        user_liked_count = Recipe.objects.filter(likes=user).count()
        user_saved_count = Recipe.objects.filter(favorites=user).count()

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


    return render(request, 'index.html', context)

def meal_type_recipes(request, meal_type_id):
    recipes = Recipe.objects.filter(meal_types__id=meal_type_id)
    return render(request, 'recipes_list.html', {'recipes': recipes})

def cuisine_recipes(request, cuisine_id):
    cuisine = get_object_or_404(Cuisine, id=cuisine_id)
    recipes = Recipe.objects.filter(cuisine=cuisine)
    return render(request, 'recipes_list.html', {
        'recipes': recipes,
        'filter_type': f"Cuisine: {cuisine.name}"
    })

def allergy_recipes(request, allergy_id):
    allergy = get_object_or_404(AllergyTag, id=allergy_id)
    recipes = Recipe.objects.filter(allergy_tags=allergy)
    return render(request, 'recipes/recipes_list.html', {
        'recipes': recipes,
        'filter_type': f"Allergy: {allergy.name}"
    })

@login_required
def my_likes(request):
    recipes = request.user.liked_recipes.all()
    return render(request, 'my_likes.html', {'recipes': recipes})

@login_required
def my_saves(request):
    recipes = request.user.favorite_recipes.all()
    return render(request, 'my_saves.html', {'recipes': recipes})
