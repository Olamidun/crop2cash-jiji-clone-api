from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('create_item', views.CreateItemAPIView.as_view()),
    path('list_items_for_sellers', views.LisAllItemsForSellerAPIView.as_view()),
]