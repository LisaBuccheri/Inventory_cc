from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement, Purchases

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"

class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"

class PurchasesForm(forms.ModelForm):
    class Meta:
        model = Purchases
        fields = "__all__"