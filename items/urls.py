from django.urls import include, path
from . import views

app_name = 'items'

urlpatterns = [
    path('create_item', views.CreateItemAPIView.as_view()),
    path('all_items', views.ListAllItemsAPIView.as_view()),
    path('list_items_for_sellers', views.LisAllItemsForSellerAPIView.as_view()),
    path('<int:id>', views.ItemDetailAPIView.as_view()),
    path('<int:id>/create_buyer', include('buyers.urls'))
]