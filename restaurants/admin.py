from django.contrib import admin
from .models import Restaurant, Item, FavourateRestaurant, FavourateItem

admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(FavourateRestaurant)
admin.site.register(FavourateItem)

# Register your models here.
