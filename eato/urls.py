"""
URL configuration for eato project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from eato_app.views.home import home, meal_type_recipes, cuisine_recipes, allergy_recipes  # noqa
from eato_app.views.recipes.recipes_list import recipes_list
from eato_app.views.recipes.add_recipe import add_recipe
from eato_app.views.registration.signup import signup
from eato_app.views.recipes.search import recipe_search
from eato_app.views.recipes.recipe_details import recipe_details, edit_recipe, delete_recipe  # noqa
from eato_app.views.views import toggle_like, toggle_save, random_recipe, crash_test  # noqa
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', home, name='index'),
    path('admin/', admin.site.urls),
    path('recipes/', recipes_list, name='recipes_list'),
    path('recipes/add/', add_recipe, name='add_recipe'),
    path('recipes/<int:recipe_id>/', recipe_details, name='recipe_details'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', next_page='index'), name='login'),  # noqa
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # noqa
    path('meal-type/<int:meal_type_id>/', meal_type_recipes, name='meal_type_recipes'),  # noqa
    path('cuisine/<int:cuisine_id>/', cuisine_recipes, name='cuisine_recipes'),
    path('allergy/<int:allergy_id>/', allergy_recipes, name='allergy_recipes'),
    path('search/', recipe_search, name='recipe_search'),
    path('recipes/<int:recipe_id>/like/', toggle_like, name='toggle_like'),
    path('recipes/<int:recipe_id>/save/', toggle_save, name='toggle_save'),
    path('random-recipe/', random_recipe, name='random_recipe'),
    path('recipes/<int:recipe_id>/edit/', edit_recipe, name='edit_recipe'),
    path('recipes/<int:recipe_id>/delete/', delete_recipe, name='delete_recipe'),  # noqa
    path('crash/', crash_test),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler404 = 'eato_app.views.errors.custom_404_view'
