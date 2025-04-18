from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from ...models import Recipe, RecipeIngredient, Ingredient
from django.contrib import messages

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
            'meal_types': forms.CheckboxSelectMultiple(),
            'allergy_tags': forms.CheckboxSelectMultiple(),
            'cuisines': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'instructions': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
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

            # 🔥 Save ingredients
            names = request.POST.getlist('ingredient_name')
            quantities = request.POST.getlist('ingredient_quantity')
            units = request.POST.getlist('ingredient_unit')
            print("Names:", names)
            for name, quantity, unit in zip(names, quantities, units):
                if name.strip():  # skip empty rows
                    ingredient_obj, created = Ingredient.objects.get_or_create(name=name.strip())
                    RecipeIngredient.objects.create(
                        recipe=recipe,
                        ingredient=ingredient_obj,
                        quantity=quantity,
                        unit=unit
                    )

            messages.success(request, "Recipe created successfully!")
            return redirect('recipes_list')
    else:
        form = RecipeForm()

    return render(request, 'recipes/add_recipe.html', {'form': form})
