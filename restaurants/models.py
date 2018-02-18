from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    openingtime = models.TimeField()
    closingtime = models.TimeField()
    logo = models.TextField()
    
    def __str__(self):
        return self.name
