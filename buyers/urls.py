from django.urls import path
from . import views

app_name = 'buyers'

urlpatterns = [
    path('', views.CreateInterestedBuyerAPIView.as_view()),
    path('buyer_count', views.buyer_count, name='buyer-count')
]