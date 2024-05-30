from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100, default="", unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=100, default="")
    unit_price = models.FloatField(default=0)

    def __str__(self):
        return f"""
            name={self.name};
            qty={self.quantity};
            unit={self.unit};
            unit_price={self.unit_price}
        """

class MenuItem(models.Model):
    title = models.CharField(max_length=100, default="", unique=True)
    price = models.FloatField(default=0.00)

    def available(self):
        return all(x.enough_ingredients() for x in self.requirements.all())

    def __str__(self):
        return f"{self.title}; {self.price} €"

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, default=None, related_name='requirements')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, default=None)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return f"menu_item=[{self.menu_item.__str__()}]; ingredient={self.ingredient.name}; qty={self.quantity}"
    
    def enough_ingredients(self):
        return self.ingredient.quantity >= self.quantity

class Purchases(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, default=None)
    time_stamp  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"menu_item[{self.menu_item.__str__()}];  time={self.time_stamp}"
    
