from ..models import MealType, Cuisine

def global_filters(request):
    return {
        'meal_types': MealType.objects.all(),
        'cuisines': Cuisine.objects.all(),
    }