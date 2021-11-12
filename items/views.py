from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics, serializers
import items

from items.models import Items

from .serializers import CreateItemSerializer, ItemListSerializer

# Create your views here.

class CreateItemAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = CreateItemSerializer

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


# class ListAllItemsForSellerAPIView(APIView):
#     permission_classes = (IsAuthenticated, )
#     def get(self, request):
#         try:
#             items = Items.objects.filter(seller=self.request.user)
#             print(items)
#             serializer = ItemListSerializer(items)
#             return Response(serializer.data)
#         except Items.DoesNotExist:
#             return Response({"error": "This Item does not exist"})

class LisAllItemsForSellerAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ItemListSerializer
    def get_queryset(self):
        items = Items.objects.filter(seller=self.request.user)
        return items