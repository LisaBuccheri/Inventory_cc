from typing import Any
from django.db.models import Sum
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from inventory_app.models import Ingredient, MenuItem, RecipeRequirement, Purchases
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchasesForm

class Home(LoginRequiredMixin, TemplateView):
  template_name = 'home.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['menuItems'] = MenuItem.objects.all()
    context['ingredients'] = Ingredient.objects.all()
    context['purchases'] = Purchases.objects.all()
    return context

class IngredientView(LoginRequiredMixin, ListView):
  model = Ingredient
  template_name = 'ingredient_list.html'
  fields = ['name', 'quantity', 'unit_price']

class IngredientCreate(LoginRequiredMixin, CreateView):
  model = Ingredient
  fields = ['name', 'quantity', 'unit_price']
  template_name = 'ingredient_form.html'
  success_url = '/ingredient/'

class IngredientUpdate(LoginRequiredMixin, UpdateView):
  model = Ingredient
  template_name = 'ingredient_update_form.html'
  success_url = '/ingredient/'
  form_class = IngredientForm

class IngredientDelete(LoginRequiredMixin, DeleteView):
  model = Ingredient
  template_name = 'ingredient_confirm_delete.html'
  success_url = '/ingredient/'

class MenuItemView(LoginRequiredMixin, ListView):
  model = MenuItem
  template_name = 'menu.html'
  context_object_name = 'menuItems'

class MenuItemCreate(LoginRequiredMixin, CreateView):
  model = MenuItem
  fields = ['title', 'price']
  template_name = 'menu_form.html'
  success_url = '/menu/'

class MenuItemUpdate(LoginRequiredMixin, UpdateView):
  model = MenuItem
  template_name = 'menu_update_form.html'
  success_url = '/menu/'
  form_class = MenuItemForm

class MenuItemDelete(LoginRequiredMixin, DeleteView):
  model = MenuItem
  template_name = 'menu_confirm_delete.html'
  success_url = '/menu/'

class RecipeRequirement(LoginRequiredMixin, CreateView):
  model = RecipeRequirement
  template_name = 'recipe_requirement.html'
  form_class = RecipeRequirementForm
  success_url = '/menu/'

class PurchasesView(LoginRequiredMixin, ListView):
  model = Purchases
  template_name = 'purchases.html'
  form_class = PurchasesForm
  context_object_name = 'purchases'
  ordering = ['-time_stamp']

class PurchasesCreate(LoginRequiredMixin, TemplateView):
  model = Purchases
  form_class = PurchasesForm
  template_name = 'purchases_form.html'
  success_url = '/purchases/'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['menu_items'] = [x for x in MenuItem.objects.all() if x.available()]
    return context
  
  def post(self, request):
    menu_item_id = request.POST.get('menu_item')
    menu_item = MenuItem.objects.get(pk=menu_item_id)
    requirements = menu_item.requirements
    purchase = Purchases(menu_item=menu_item)

    for requirement in requirements.all():
      required_indredient = requirement.ingredient
      required_indredient.quantity -= requirement.quantity
      required_indredient.save()
    
    purchase.save()
    return redirect('/purchases/') 

class SalesView(LoginRequiredMixin, TemplateView):
  template_name = 'sales.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['purchases'] = Purchases.objects.all()
    revenue = Purchases.objects.all().aggregate(
      revenue=Sum('menu_item__price'))["revenue"]
    total_cost = 0
    for purchase in Purchases.objects.all():
      for requirement in purchase.menu_item.requirements.all():
        total_cost += requirement.ingredient.unit_price * requirement.quantity

    context['revenue'] = revenue
    context['total_cost'] = total_cost
    context['profit'] = revenue - total_cost
    
    return context


def log_out(request):
    logout(request)
    return redirect("/")