from .models import Items
from django import dispatch
from django.core.cache import cache
from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save

# This signals clears the cache if an item has been deleted from the db
@receiver(post_delete, sender=Items, dispatch_uid='item_deleted')
def invalidate_cache_after_item_delete(sender, **kwargs):
    cache.delete('items')

# This signals clears the cache if an item has been added to the db
@receiver(post_save, sender=Items, dispatch_uid='item_create')
def invalidate_cache_after_item_create(sender, **kwargs):
    cache.delete('items')


