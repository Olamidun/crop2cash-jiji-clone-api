from django.shortcuts import HttpResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import CreateInterestedBuyerSerializer

from items.serializers import ItemListSerializer
from items.models import Items


# Create your views here.


class CreateInterestedBuyerAPIView(generics.CreateAPIView):
    serializer_class = CreateInterestedBuyerSerializer

    def perform_create(self, serializer):
        item = Items.objects.get(id=self.kwargs['id'])
        print(item)
        serializer.save(item=item)
        



def buyer_count(request):
    items = Items.objects.filter(pk=1).count()
    print(items)
    # return HttpResponse(items)