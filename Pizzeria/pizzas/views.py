from django.shortcuts import render

from .models import Topping

def index(request):
    """The home page for Pizzas."""
    return render(request, 'pizzas/index.html')

def toppings(request):
    """Show all toppings."""
    toppings = Topping.objects.order_by('date_added')
    context = {'toppings': toppings}
    return render(request, 'pizzas/toppings.html', context)

def topping(request, topping_id):
    """Show a single topping and all its entries."""
    topping = Topping.objects.get(id=topping_id)
    entries = topping.entry_set.order_by('-date_added')
    context = {'topping': topping, 'entries': entries}
    return render(request, 'pizzas/topping.html', context)
