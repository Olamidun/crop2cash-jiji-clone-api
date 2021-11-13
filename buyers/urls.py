from django.urls import path
from . import views

app_name = 'buyers'

urlpatterns = [
    # path('<int:id>/create_buyer/', views.CreateInterestedBuyerAPIView.as_view()),
    path('<item_id>/create_buyer', views.CreateBuyerForItemAPIView.as_view()),
    path('<int:item_id>/<int:buyer_id>/choose_buyer', views.BuyerForAnItemAPIView.as_view()),
    path('<int:item_id>/<int:buyer_id>/something', views.test_something),
]

# 1 and 3