from django.conf.urls.static import static
from django.urls import path

from RecipeBook import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('all_recipes/', views.all_recipes, name='all_recipes'),
    path('users/', views.show_users, name='show_users'),
    path('entrance/', views.entrance, name='entrance'),
    path('all_recipes/<int:recipe_id>/', views.one_recipe, name='one_recipe'),
    path('add_category/', views.add_category, name='add_category'),
    path('show_categories/', views.show_categories, name='show_categories'),
    path('recipe_category/', views.recipe_category, name='recipe_category'),
    path('show_categories/<int:category_id>', views.recipe_by_category, name='recipe_by_category')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
