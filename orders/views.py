from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Sum

from .models import Food, Toppings, Cart, Order
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html")
    else:
        context= {
            "user": request.user,
            "items": Food.objects.all(),
            "toppings": Toppings.objects.all()
        }
        return render(request, "orders/index.html", context)

def food(request, food_id):
    context = {
        "item": Food.objects.get(pk=food_id),
        "toppings_allowed": range( Food.objects.get(pk=food_id).toppings_allowed),
        "toppings": Toppings.objects.all()
    }
    return render(request, "orders/add.html", context)


def ordered(request, food_id):
    food = Food.objects.get(pk=food_id)
    item = Cart(item = food)
    item.save()
    user = request.user
    item.user.add(user)
    for i in range(food.toppings_allowed):
        if i==0:
            top = int(request.POST.get("topping_1"))
            topping = Toppings.objects.get(pk=top)
            topping.pizza.add(item)
        elif i==1:
            top = int(request.POST["topping_2"])
            topping = Toppings.objects.get(pk=top)
            topping.pizza.add(item)
        elif i==2:
            top = int(request.POST["topping_3"])
            topping = Toppings.objects.get(pk=top)
            topping.pizza.add(item)

    context= {
        "user": request.user,
        "items": Food.objects.all(),
        "toppings": Toppings.objects.all()
    }
    return render(request, "orders/index.html", context)

def cart(request):
    user = request.user
    orders = user.cart.all()
    items = user.cart.values_list('item', flat=True)
    total = 0
    for item in items:
        total += Food.objects.get(pk=item).cost

    context ={
        "orders": user.cart.all(),
        "total": total
    }
    return render(request, "orders/cart.html", context)

def poder(request):
    user = request.user
    orders = user.cart.all()
    for order in orders:
        food = order.item
        o = Order(item = food)
        o.save()
        o.user.add(user)
        toppings = order.toppings.all()
        for t in toppings:
            t.order.add(o)
        order.delete()

    context= {
        "user": request.user,
        "items": Food.objects.all(),
        "toppings": Toppings.objects.all()
    }
    return render(request, "orders/index.html", context)

def status(request):
    user = request.user
    context = {
        "orders": user.orders.all()
    }
    return render(request, "orders/status.html", context)

def login_auth(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})

def register(request):
    firstName = request.POST["firstName"]
    lastName = request.POST["lastName"]
    email = request.POST["email"]
    username = request.POST["username"]
    password = request.POST["password"]
    u = User.objects.create_user(username=username, email=email, password=password)
    u.save()
    u.first_name = firstName
    u.last_name = lastName
    u.save()
    if u is not None:
        login(request, u)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/register.html", {"message": "Invalid credentials."})

def sign_up(request):
    return render(request, "orders/register.html")
