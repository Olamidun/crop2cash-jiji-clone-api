from .models import Items
from drf_yasg import openapi
from buyers.models import Buyers
from django.conf import settings
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from .serializers import ListAllItemsForABuyerSerializer
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from buyers.serializers import CreateInterestedBuyerSerializer
from .serializers import CreateItemSerializer, ItemDetailSerializer, ItemListSerializer

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class CreateItemAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = CreateItemSerializer

    # # This decorator ensures the request body contains image upload option on swagger
    @swagger_auto_schema(request_body=CreateInterestedBuyerSerializer, operation_description='Upload file...',)
    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


# Lists all the items in the database that hasn't been sold
class ListAllItemsAPIView(generics.ListAPIView):
    serializer_class = ItemListSerializer
    def get_queryset(self):

        '''
        Checks if queryset of items has been cached before, if it has, the list is pulled from cache and returns it as response, if not, it gets the queryset from db, saves it to cache and then returns it as response
        '''
        if 'items' in cache:
            items = cache.get('items')
            return items
        else:
            items = Items.objects.filter(has_been_sold=False).select_related('seller').order_by('-date_added')
            cache.set('items', items, timeout=CACHE_TTL)
            return items


# Lists all the Items a seller has created
class LisAllItemsForSellerAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ItemListSerializer
    def get_queryset(self):
        items = Items.objects.filter(seller=self.request.user).select_related('sold_to')
        return items


class ItemDetailAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    # Retrieves a single item
    def get(self, request, id):

        # Tries to get the item with the given id and logged in user from the db
        try:
            item = Items.objects.get(id=id, seller=self.request.user)
            serializer = ItemDetailSerializer(item)
            return Response(serializer.data)

        # Returns an appropriate error response if the item cannot be found
        except Items.DoesNotExist:
            return Response({'error': "This item does not exist for this user"}, status=status.HTTP_404_NOT_FOUND)

    
    def delete(self, request, id):
        try:
            Items.objects.get(id=id, seller=self.request.user).delete()
            return Response({'message': 'Item has been deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Items.DoesNotExist:
            return Response({'error': 'This item does not exist for this user'}, status=status.HTTP_404_NOT_FOUND)


'''

This endpoint should be called when getting the list of items a buyer has shown interest in. 
A query parameter "?email=<email_address>" should be appended to it.

Since buyers are not going to be authenticated, when a buyer shows interest in an item for the first time, their email can be saved into local storage / cookies on the frontend for a period of time so that when next they visit the website, the frontend checks if the email is still in local storage / cookies, and then uses it as query parameter for this endpoint to return list of items the buyer has shown interest in. If it is not, the frontend can ask for their email (Ensure to inform the buyer to use the email they used on their first visit).
If a buyer on their subsequent visits shows interest in an item before attempting to see the list of items they have shown interest in, then we can use the email they provided instead of asking for it again ....

'''
class ItemsForABuyer(APIView):
    param = openapi.Parameter('email', openapi.IN_QUERY, description="Email parameter to get a buyer's list of interested items", type=openapi.TYPE_STRING)
    @swagger_auto_schema(manual_parameters=[param])
    # Retrieves a single item
    def get(self, request):
        # Tries to get the Buyer with the given id and logged in user from the db
        email = self.request.query_params.get('email')
        try:
            buyer = Buyers.objects.get(email=email)
            serializer = ListAllItemsForABuyerSerializer(buyer)
            return Response(serializer.data)

        # Returns an appropriate error response if the buyer cannot be found
        except Buyers.DoesNotExist:
            return Response({'error': "This buyer does not exist"}, status=status.HTTP_404_NOT_FOUND)

