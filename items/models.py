from django.db import models
from django.conf import settings

# Create your models here.

class Items(models.Model):
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='item_image')
    has_been_sold = models.BooleanField(default=False)
    

    def __str__(self):
        return f'{self.seller.email} {self.name}'

