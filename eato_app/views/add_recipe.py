from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from ..models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'description',
            'image',
            'cuisine',
            'meal_types',
            'allergy_tags',
            'instructions',
        ]
        widgets = {
            'meal_types': forms.CheckboxSelectMultiple,
            'allergy_tags': forms.CheckboxSelectMultiple,
            'cuisines': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'ingredients': forms.Textarea(attrs={'rows': 3}),
            'instructions': forms.Textarea(attrs={'rows': 5}),
        }

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()
            form.save_m2m()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})
