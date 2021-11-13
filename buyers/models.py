from django.db import models
from items.models import Items

# Create your models here.


class Buyers(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    location = models.CharField(max_length=200)
    item = models.ForeignKey(Items, related_name='buyers', on_delete=models.CASCADE)


    def __str__(self):
        return f'Buyer {self.name}'