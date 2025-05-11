from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient, Cuisine, MealType, AllergyTag, Like, Favorite  # noqa


# Register your models here.
# Allows adding ingredients inside the recipe form
class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'cuisine')
    search_fields = ('title', 'description', 'cuisine__name')
    list_filter = ('meal_types', 'allergy_tags', 'cuisine')
    # Allows adding ingredients in the same form
    inlines = [RecipeIngredientInline]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(MealType)
admin.site.register(AllergyTag)
admin.site.register(Cuisine)
admin.site.register(Like)
admin.site.register(Favorite)
