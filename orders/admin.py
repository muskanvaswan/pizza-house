from django.contrib import admin
from .models import Food, Toppings, Cart, Order

# Register your models here.
admin.site.register(Food)
admin.site.register(Toppings)
admin.site.register(Cart)
admin.site.register(Order)
