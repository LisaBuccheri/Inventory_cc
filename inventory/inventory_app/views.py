from django.shortcuts import render
from inventory_app.models import Ingredient, MenuItem, RecipeRequirement, Purchases
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchasesForm


def home(request):
  context = {
    'menuItems': MenuItem.objects.all(),
    'ingredients': Ingredient.objects.all(),
    'purchases': Purchases.objects.all()
  }
  return render(request, 'home.html', context)

class IngredientView(ListView):
  model = Ingredient
  template_name = 'ingredient_list.html'
  fields = ['name', 'quantity', 'unit_price']

class IngredientCreate(CreateView):
  model = Ingredient
  fields = ['name', 'quantity', 'unit_price']
  template_name = 'ingredient_form.html'
  success_url = '/ingredient/'

class IngredientUpdate(UpdateView):
  model = Ingredient
  template_name = 'ingredient_update_form.html'
  success_url = '/ingredient/'
  form_class = IngredientForm

class IngredientDelete(DeleteView):
  model = Ingredient
  template_name = 'ingredient_confirm_delete.html'
  success_url = '/ingredient/'

class MenuItemView(ListView):
  model = MenuItem
  template_name = 'menu.html'
  context_object_name = 'menuItems'

class MenuItemCreate(CreateView):
  model = MenuItem
  fields = ['title', 'price']
  template_name = 'menu_form.html'
  success_url = '/menu/'

class MenuItemUpdate(UpdateView):
  model = MenuItem
  template_name = 'menu_update_form.html'
  success_url = '/menu/'
  form_class = MenuItemForm

class MenuItemDelete(DeleteView):
  model = MenuItem
  template_name = 'menu_confirm_delete.html'
  success_url = '/menu/'

class RecipeRequirement(CreateView):
  model = RecipeRequirement
  template_name = 'recipe_requirement.html'
  form_class = RecipeRequirementForm
  success_url = '/menu/'

class PurchasesView(ListView):
  model = Purchases
  template_name = 'purchases.html'
  form_class = PurchasesForm
  context_object_name = 'purchases'
  ordering = ['-time_stamp']

class PurchasesCreate(CreateView):
  model = Purchases
  form_class = PurchasesForm
  template_name = 'purchases_form.html'
  success_url = '/purchases/'

