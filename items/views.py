from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework import generics, status

from items.models import Items

from .serializers import CreateItemSerializer, ItemDetailSerializer, ItemListSerializer

# Create your views here.

class CreateItemAPIView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )
    parser_classes = (MultiPartParser, )
    serializer_class = CreateItemSerializer

    @swagger_auto_schema(operation_description='Upload file...',)
    @action(detail=True, methods=['post'],)
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


    def delete(self, request, id):
        try:
            Items.objects.get(id=id, seller=self.request.user).delete()
            return Response({'message': 'Item has been deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Items.DoesNotExist:
            return Response({'message': 'This item does not exist for this user'}, status=status.HTTP_404_NOT_FOUND)

