from django.contrib import admin

from .models import User, Categories, Recipes, RecipeCategoryFilter


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_date_add')


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('category_name',)


@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'recipe_description', 'author')


@admin.register(RecipeCategoryFilter)
class RecipeCategoryFilterAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'category')

# admin.site.register(User, UserAdmin)
# admin.site.register(Categories, CategoriesAdmin)
# admin.site.register(Recipes, RecipesAdmin)
# admin.site.register(RecipeCategoryFilter, RecipeCategoryFilterAdmin)
