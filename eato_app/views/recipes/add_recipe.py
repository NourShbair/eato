from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from ...models import Recipe, RecipeIngredient, Ingredient
from django.contrib import messages


# Custom form class for Recipe model
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        # Define which fields from the Recipe model should be included in the form   # noqa
        fields = [
            'title',
            'description',
            'image',
            'cuisine',
            'meal_types',
            'allergy_tags',
            'instructions',
            ]

        # Customize form widgets for specific fields
        widgets = {
            'meal_types': forms.CheckboxSelectMultiple(),
            'allergy_tags': forms.CheckboxSelectMultiple(),
            'cuisines': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'instructions': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),   # noqa
        }

    # Custom validation for image field
    def clean_image(self):
        image = self.cleaned_data.get('image')
        # Ensure an image is provided
        if not image:
            raise forms.ValidationError("An image is required for your recipe.")   # noqa
        return image


# ensures only logged-in users can access this view
@login_required
def add_recipe(request):
    if request.method == 'POST':
        # Create form instance with submitted data, including files
        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            # Create recipe object but don't save to database yet
            recipe = form.save(commit=False)
            # Set the creator of the recipe
            recipe.created_by = request.user
            # Save the recipe to the database
            recipe.save()
            # Save many-to-many relationships
            form.save_m2m()

            # Handle ingredients
            # Get lists of ingredient details from POST data
            names = request.POST.getlist('ingredient_name')
            quantities = request.POST.getlist('ingredient_quantity')
            units = request.POST.getlist('ingredient_unit')

            # Process each ingredient
            for name, quantity, unit in zip(names, quantities, units):
                if name.strip():  # Only process if ingredient name is not empty   # noqa
                    # Get or create ingredient in the database
                    ingredient_obj, created = Ingredient.objects.get_or_create(name=name.strip())   # noqa
                    # Create recipe-ingredient relationship
                    RecipeIngredient.objects.create(
                        recipe=recipe,
                        ingredient=ingredient_obj,
                        quantity=quantity,
                        unit=unit
                    )

            # Show success message to user
            messages.success(request, "Recipe created successfully!")
            # Redirect to recipes list page
            return redirect('recipes_list')
    else:
        # If GET request, create empty form
        form = RecipeForm()

    # Render the add recipe template with the form
    return render(request, 'recipes/add_recipe.html', {'form': form})
