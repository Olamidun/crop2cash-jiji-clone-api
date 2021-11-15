from . import views
from django.urls import path

app_name = 'items'

urlpatterns = [
    path('create_item', views.CreateItemAPIView.as_view(), name='create_item'),
    path('all_items', views.ListAllItemsAPIView.as_view(), name='list_items'),
    path('list_items_for_sellers', views.LisAllItemsForSellerAPIView.as_view(), name='list_items_for_user'),
    path('<int:id>', views.ItemDetailAPIView.as_view()),
    path('list_all_items_for_buyer', views.ItemsForABuyer.as_view(), name='list_all_items_for_buyers'),
]