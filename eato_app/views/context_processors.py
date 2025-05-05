from ..models import MealType, Cuisine

def global_filters(request):
    return {
        # Get all meal types from database
        # This will be available in all templates as {{ meal_types }}
        'meal_types': MealType.objects.all(),
        
        # Get all cuisines from database
        # This will be available in all templates as {{ cuisines }}
        'cuisines': Cuisine.objects.all(),
    }
