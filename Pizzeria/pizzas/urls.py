"""Defines URL patterns for pizzas."""

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('toppings/', views.toppings, name='toppings'),
    # Detail page for a single topic.
    path('toppings/<int:topping_id>/', views.topping, name='topping'),
]
