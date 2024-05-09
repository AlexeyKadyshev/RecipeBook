from random import choices
import logging
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

from clients_recipes.forms import LoginForm, EntranceForm, AddRecipeForm, AddCategoryForm, RecipeCategoryFilterForm
from clients_recipes.models import User, Recipes, Categories, RecipeCategoryFilter

logger = logging.getLogger(__name__)

menu_index = [{'title': 'Войти', 'url_name': 'entrance'},
              {'title': 'Регистрация', 'url_name': 'registration'}]


def index(request):
    logger.info('Index page accessed')
    data = {
        'menu': menu_index,
        'title': 'Книга рецептов'
    }
    return render(request, 'clients_recipes/index.html', context=data)


def one_recipe(request, recipe_id):
    logger.info('Recipe page accessed')
    try:
        recipe = Recipes.objects.get(pk=recipe_id)
    except:
        return redirect('all_recipes')
    data = {'recipe': recipe}
    return render(request, 'clients_recipes/one_recipe.html', context=data)


def registration(request):
    logger.info('Registration page accessed')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            users = User.objects.all()
            users_list = [u.username for u in users]
            if username in users_list:
                logger.info('Username_error page accessed')
                return render(request, 'clients_recipes/username_error.html')
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password == confirm_password:
                user = User(username=username, password=password)
                user.save()
                logger.info('Successful_registration page accessed')
                return render(request, 'clients_recipes/successful_registration.html')
            return redirect('registration')
    else:
        form = LoginForm()

    data = {'form': form}
    return render(request, 'clients_recipes/registration.html', data)


def all_recipes(request):
    # Эту же функцию можно использовать для отображения всех рецептов, а не только 5 по условию задания
    logger.info('All_recipes page accessed')
    recipes = Recipes.objects.all()
    if recipes:
        recipes = choices(recipes, k=5)
    # recipes = Recipes.objects.all()            # Для отображения всех рецептов
    data = {'recipes': recipes}
    return render(request, 'clients_recipes/all_recipes.html', context=data)


def entrance(request):
    logger.info('Entrance page accessed')
    if request.method == 'POST':
        form = EntranceForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            dict_users = {}
            users = User.objects.all()
            for u in users:
                dict_users[u.username] = u.password
            if username in dict_users and dict_users[username] == password:
                return redirect('all_recipes')
            return redirect('entrance')
    else:
        form = EntranceForm()

    data = {'form': form}
    return render(request, 'clients_recipes/entrance.html', data)


def add_recipe(request):
    logger.info('Add_recipe page accessed')
    if request.method == 'POST':
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_recipes')
    else:
        form = AddRecipeForm()
    data = {'form': form}
    return render(request, 'clients_recipes/add_recipe.html', data)


def add_category(request):
    logger.info('Add_category page accessed')
    if request.method == 'POST':
        form = AddCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_recipe')
    else:
        form = AddCategoryForm()
    data = {'form': form}
    return render(request, 'clients_recipes/add_category.html', context=data)


def show_categories(request):
    logger.info('Show_categories page accessed')
    categories = Categories.objects.all()
    data = {'categories': categories}
    return render(request, 'clients_recipes/show_categories.html', context=data)


# def recipe_by_category(request, category_id):
#     category = Categories.objects.get(pk=category_id)
#     try:
#         recipes = RecipeCategoryFilter.objects.filter(category=category)
#     except:
#         return redirect('show_categories')
#     data = {'recipes': recipes,
#             'category': category}
#     return render(request, 'clients_recipes/recipe_by_category.html', context=data)


# def recipe_category(request):
#     if request.method == 'POST':
#         form = RecipeCategoryFilterForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # cat = Categories.objects.get(pk=form.category)
#             # print(cat)
#             # cat.save()
#             return redirect('recipe_category')
#     else:
#         form = RecipeCategoryFilterForm()
#     data = {'form': form}
#     return render(request, 'clients_recipes/recipe_category.html', data)


def recipe_category(request):
    if request.method == 'POST':
        form = RecipeCategoryFilterForm(request.POST)
        if form.is_valid():
            recipe_ad = form.cleaned_data['recipe']
            category_id = form.cleaned_data['category']
            recipe = Recipes.objects.get(pk=recipe_ad)
            category = Categories.objects.get(pk=category_id)
            new_data = RecipeCategoryFilter(recipe=recipe, category=category)
            new_data.save()
            return redirect('recipe_category')
    else:
        form = RecipeCategoryFilterForm()

    data = {'form': form}
    return render(request, 'clients_recipes/recipe_category.html', data)


def recipe_by_category(request, category_id):
    category = Categories.objects.get(pk=category_id)
    try:
        recipes = RecipeCategoryFilter.objects.filter(category=category)
        recipes = [recipe.recipe for recipe in recipes]
    except:
        return redirect('show_categories')
    data = {'recipes': recipes,
            'category': category}
    return render(request, 'clients_recipes/recipe_by_category.html', context=data)


def show_users(request):
    dict_users = {}
    list_users = []
    users = User.objects.all()
    for u in users:
        dict_users[u.username] = u.password

    for key, value in dict_users.items():
        list_users.append((key, value))

    data = {'users': list_users}
    return render(request, 'clients_recipes/users.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
