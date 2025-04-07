from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Recipe, MealType, Cuisine, AllergyTag, Like, Favorite

from django.db.models import Count

# @login_required
def home(request):
    user = request.user
    meal_types = MealType.objects.all()
    cuisines = Cuisine.objects.all()
    allergies = AllergyTag.objects.all()
    recent_recipes = Recipe.objects.order_by('-created_at')[:5]  # Latest 5 recipes

    user_recipe_count = Recipe.objects.filter(created_by=user).count()
    user_liked_count = Like.objects.filter(user=user).count()
    user_saved_count = Favorite.objects.filter(user=user).count()

    context = {
        'meal_types': meal_types,
        'cuisines': cuisines,
        'allergies': allergies,
        'recent_recipes': recent_recipes,
        'user_recipe_count': user_recipe_count,
        'user_liked_count': user_liked_count,
        'user_saved_count': user_saved_count,
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
    return render(request, 'recipes_list.html', {
        'recipes': recipes,
        'filter_type': f"Allergy: {allergy.name}"
    })