from django.shortcuts import render
from django.views import generic
from rest_framework import permissions, serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics

from items.models import Items

from .serializers import CreateItemSerializer, ItemDetailSerializer, ItemListSerializer

# Create your views here.

class CreateItemAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = CreateItemSerializer

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class ListAllItemsAPIView(generics.ListAPIView):
    serializer_class = ItemListSerializer

    def get_queryset(self):
        items = Items.objects.filter(has_been_sold=False).order_by('-date_added')
        return items


class LisAllItemsForSellerAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ItemListSerializer
    def get_queryset(self):
        items = Items.objects.filter(seller=self.request.user)
        return items


class ItemDetailAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request, id):
        try:
            item = Items.objects.get(id=id, seller=self.request.user)
            serializer = ItemDetailSerializer(item)
            return Response(serializer.data)
        except Items.DoesNotExist:
            return Response({'error': "This item does not exist for this user"})

