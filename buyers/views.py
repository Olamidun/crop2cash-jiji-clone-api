from .models import Buyers
from items.models import Items
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from .serializers import CreateInterestedBuyerSerializer

# Create your views here.

class CreateBuyerForItemAPIView(APIView):

    # This decorator ensures the request body is displayed on swagger
    @swagger_auto_schema(request_body=CreateInterestedBuyerSerializer, responses={
        '200': 'Ok Request',
        '400': "Bad request"
    }, operation_description="Create interested buyer for an item")
    def post(self, request):
        context = {}

        # Try and get an item with the given id from database
        try:
            # item = Items.objects.get(id=item_id)
            print(type(request.data))
            serializer = CreateInterestedBuyerSerializer(data = request.data)  
            if serializer.is_valid():
                serializer.save()
                context["message"] = "Buyer has been added"
                context["data"] = serializer.data
                return Response(context, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # return an appropriate message if the item does not exist in the db
        except Items.DoesNotExist:
            return Response({"message": "This item does not exist for this user"}, serializer.data)


class ChooseBuyerForAnItemAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    @swagger_auto_schema(operation_description="Choose a buyer for an item")
    def patch(self, request, item_id, buyer_id):

        '''
        
        Gets the item and buyer with the given ids from the db, and then assign the buyer as the one the item is sold to
        
        '''
        try:
            '''
            This is a performance booster. It gets the foreignkey attribute 'sold_to' when getting the item instance. With this, django won't hit the db when executing "item.sold_to"
            '''
            item = Items.objects.select_related('sold_to').get(id=item_id)
            buyer = Buyers.objects.get(id=buyer_id)
            if item.seller == self.request.user:
                item.sold_to = buyer
                item.has_been_sold = True
                item.save()
                return Response({"message": "This buyer has been chosen as the owner of this item"}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({"message": "You did not create this item, so you cannot choose a user"})
        except Items.DoesNotExist:
            return Response({"message": "This item does not exist for this user"})


def test_something(request, item_id, buyer_id):
    # item = Items.objects.select_related('sold_to').get(id=item_id)
    # print(item.sold_to)
    # buyer = Buyers.objects.get(id=buyer_id)
    item = Items.objects.get(id=item_id)
    print(item.sold_to)
    buyer = Buyers.objects.get(id=buyer_id)

