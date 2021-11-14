from django.db import models
from items.models import Items

# Create your models here.

class Buyers(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    location = models.CharField(max_length=200)
    item = models.ManyToManyField(Items, related_name='buyers')

    def __str__(self):
        return f'Buyer {self.name}'

    class Meta:
        # This ensures this db table named "Buyers" and not the default "Buyerss" django would name it
        verbose_name_plural = 'Buyers'