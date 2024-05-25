from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100, default="")
    quantity = models.IntegerField(default=0)
    unit_price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.name} - qty={self.quantity} - price={self.unit_price}"

class MenuItem(models.Model):
    title = models.CharField(max_length=100, default="")
    price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.title}; {self.price} €"

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, default=None, related_name='requirements')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, default=None)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return f"menu_item=[{self.menu_item.__str__()}]; ingredient={self.ingredient.name}; qty={self.quantity}"

class Purchases(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, default=None)
    time_stamp  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"menu_item[{self.menu_item.title}];  time={self.time_stamp}"
    
