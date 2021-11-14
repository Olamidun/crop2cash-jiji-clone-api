from django.urls import path
from . import views

app_name = 'buyers'

urlpatterns = [
    # url to add interested buyer for an item
    path('create_buyer', views.CreateBuyerForItemAPIView.as_view()),

    # url to choose which buyer the seller wants to sell to out of the list of buyers
    path('<int:item_id>/<int:buyer_id>/choose_buyer', views.ChooseBuyerForAnItemAPIView.as_view()),
    path('<int:item_id>/<int:buyer_id>/something', views.test_something),
]
