from django import dispatch
from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import Items


@receiver(post_delete, sender=Items, dispatch_uid='item_deleted')
def invalidate_cache_after_item_delete(sender, **kwargs):
    cache.delete('items')

@receiver(post_save, sender=Items, dispatch_uid='item_create')
def invalidate_cache_after_item_create(sender, **kwargs):
    cache.delete('items')


