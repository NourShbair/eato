from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ...models import Recipe, RecipeIngredient
from .add_recipe import RecipeForm
from django.forms import modelformset_factory


def recipe_details(request, recipe_id):
    # Get the recipe object or return 404 if not found
    recipe = get_object_or_404(Recipe, id=recipe_id)
    # Get all ingredients associated with this recipe
    ingredients = recipe.recipeingredient_set.all()

    # Prepare context data for template
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }
    # Render the recipe details template with context
    return render(request, 'recipes/recipe_details.html', context)


# View function to edit recipe
# ensures only logged-in users can access this view
@login_required
def edit_recipe(request, recipe_id):
    # Get the recipe object or return 404 if not found
    # Also ensures only the creator can edit the recipe
    recipe = get_object_or_404(Recipe, id=recipe_id, created_by=request.user)

    # Create a formset factory for handling multiple ingredients
    IngredientFormSet = modelformset_factory(
        RecipeIngredient,
        fields=('ingredient', 'quantity', 'unit'),
        extra=1  # Add one extra empty form
    )

    if request.method == 'POST':
        # Process the submitted form data
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        # Get the formset data for ingredients
        formset = IngredientFormSet(
            request.POST,
            queryset=RecipeIngredient.objects.filter(recipe=recipe)
        )
        print(form.is_valid() ," , ", formset)
        # Validate both form and formset
        if form.is_valid():
            # Save the main recipe form
            form.save()
            # Process ingredients
            instances = formset.save(commit=False)
            for instance in instances:
                # Associate each ingredient with the recipe
                instance.recipe = recipe
                instance.save()
            # Save many-to-many relationships
            formset.save_m2m()
            # Show success message
            messages.success(request, "Recipe updated successfully!")
            # Redirect to recipe details page
            return redirect('recipe_details', recipe_id=recipe.id)
    else:
        # For GET request, display the current recipe data
        form = RecipeForm(instance=recipe)
        # Display current ingredients
        formset = IngredientFormSet(
            queryset=RecipeIngredient.objects.filter(recipe=recipe)
        )

    # Render the edit template with forms
    return render(request, 'recipes/edit_recipe.html', {
        'form': form,
        'recipe': recipe,
        'formset': formset
    })


# ensures only logged-in users can access this view
@login_required
def delete_recipe(request, recipe_id):
    # Get the recipe object or return 404 if not found
    # Also ensures only the creator can delete the recipe
    recipe = get_object_or_404(Recipe, id=recipe_id, created_by=request.user)

    if request.method == 'POST':
        # Delete the recipe
        recipe.delete()
        # Show success message
        messages.success(request, "Recipe deleted.")
        # Redirect to recipes list page
        return redirect('recipes_list')

    # For GET request, show confirmation page
    return render(request, 'recipes/delete_recipe.html', {'recipe': recipe})
