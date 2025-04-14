from django.shortcuts import render
from django.core.paginator import Paginator
from ..models import Recipe

def recipes_list(request):
    recipes = Recipe.objects.all().order_by('-created_at')
    paginator = Paginator(recipes, 6)  # Show 6 recipes per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'recipes/recipes_list.html', {
        'page_obj': page_obj
    })