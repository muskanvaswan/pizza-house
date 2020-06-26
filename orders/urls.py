from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_auth, name="login"),
    path("register/", views.register, name="register"),
    path("sign_up", views.sign_up, name="sign_up"),
    path("logout/", views.logout_view, name="logout"),
    path("<int:food_id>", views.food, name="food"),
    path("<int:food_id>/ordered", views.ordered, name="ordered"),
    path("cart/", views.cart, name="cart"),
    path("PlaceOrder/", views.poder, name="porder"),
    path("status/", views.status, name="status")

]
