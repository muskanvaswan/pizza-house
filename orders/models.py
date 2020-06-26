from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    Sizes =[('small','S'), ('large', 'L'), ('regular', 'R')]
    Types =[( 'Regular_Pizza','Regular_Pizzas'), ('Silicate_Pizza','Silicate_Pizzas'), ('Subs','SUB'), ('Dinner_Platter','dinner_platters'), ('Pasta', 'pastas'),('salad','Salads')]
    name = models.CharField(max_length = 100)
    size = models.CharField(null= True, max_length = 10, choices=Sizes, default="regular")
    type = models.CharField(choices=Types, max_length=64)
    toppings_allowed = models.IntegerField()
    cost = models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return f"{self.name}, {self.size} - $ {self.cost}"

class Cart(models.Model):

    item = models.ForeignKey(Food, related_name="items", on_delete=models.CASCADE)
    user = models.ManyToManyField(User, related_name="cart")

    def __str__(self):
        return f" {self.item}"

class Order(models.Model):
    statuses = [('placed_order', 'PO'),('on_the_way', 'OTW'), ('delivered', 'D'), ('Cancelled','C')]
    item = models.ForeignKey(Food, related_name="orders", on_delete=models.CASCADE)
    user = models.ManyToManyField(User, related_name="orders")
    status = models.CharField( max_length = 10, choices=statuses, default="placed_order")

    def __str__(self):
        return f"Ordered {self.item}"


class Toppings(models.Model):
    name = models.CharField(max_length=64)
    pizza = models.ManyToManyField(Cart, blank=True, related_name="toppings")
    order = models.ManyToManyField(Order, blank=True, related_name="toppings")

    def __str__(self):
        return f"{self.name}"
