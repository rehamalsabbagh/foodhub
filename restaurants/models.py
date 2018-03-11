from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    openingtime = models.TimeField()
    closingtime = models.TimeField()
    logo = models.ImageField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.CharField(max_length=200)
    restaurant = models.ForeignKey(Restaurant , default=1 , on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class FavourateRestaurant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant , on_delete=models.CASCADE)

class FavourateItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Item = models.ForeignKey(Item , on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant , on_delete=models.CASCADE)