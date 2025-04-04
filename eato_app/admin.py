from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient, Cuisine, MealType, AllergyTag, Like, Favorite

# Register your models here.
class RecipeIngredientInline(admin.TabularInline):  # Allows adding ingredients inside the recipe form
    model = RecipeIngredient
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'cuisine')
    search_fields = ('title', 'description', 'cuisine__name')
    list_filter = ('meal_types', 'allergy_tags', 'cuisine')
    inlines = [RecipeIngredientInline]  # Allows adding ingredients in the same form

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(MealType)
admin.site.register(AllergyTag)
admin.site.register(Cuisine)
admin.site.register(Like)
admin.site.register(Favorite)