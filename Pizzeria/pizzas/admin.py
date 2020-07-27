from django.contrib import admin

from .models import Pizza, Topping, Entry

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Entry)
