from django.db import models
from django.db.models import Count
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Items(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='item_image')
    date_added = models.DateTimeField(auto_now_add=True)
    has_been_sold = models.BooleanField(default=False)

    # referencing the Buyers model so I can know who an item is sold to
    sold_to = models.ForeignKey('buyers.Buyers', on_delete=models.SET_NULL, null=True, blank=True)
    

    def __str__(self):
        return f'{self.seller.email} {self.name}'

    class Meta:
        # This ensures this db table is named "Items" and not the default "Itemss" django would name it
        verbose_name_plural = 'Items'


    def number_of_buyers(self):
        buyer_count = Items.objects.filter(pk=self.pk).aggregate(Count('buyers'))['buyers__count']
        return buyer_count
