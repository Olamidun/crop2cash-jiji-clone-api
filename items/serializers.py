from .models import Items
from buyers.models import Buyers
from rest_framework import serializers
from seller.serializers import SellerSerializers
from buyers.serializers import ListBuyersSerializers


class CreateItemSerializer(serializers.ModelSerializer):
    seller = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Items
        fields = ['id', 'name', 'seller', 'price', 'image', 'description']

        # configuration to ensure id is not required as part of the request
        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }


class ItemListSerializer(serializers.ModelSerializer):

    '''

    Since we want the sellers' information and number of interested buyers as part of response, I am nesting user information into the response returned by the serializer by using UserSerializers(). Same with number of interested buyers
    
    '''
    seller = SellerSerializers()
    number_of_interested_buyers = serializers.SerializerMethodField('get_number_of_buyers')

    class Meta:
        model = Items

        fields = ['id', 'name', 'seller', 'price', 'image', 'description', 'number_of_interested_buyers', 'has_been_sold']

        extra_kwargs = {
            "id":{
                "read_only": True
            }
        }


    def get_number_of_buyers(self, obj):
        buyer_count = obj.number_of_buyers()
        return buyer_count


class ListAllItemsForABuyerSerializer(serializers.ModelSerializer):
    item = ItemListSerializer(read_only=True, many=True)

    class Meta:
        model = Buyers
        fields = '__all__'


class ItemDetailSerializer(serializers.ModelSerializer):

    '''

    Apart from sellers' information, I also need the list of all the buyers interested in an item to be part of the response, hence the reason for making use of ListBuyersSerializers

    '''
    seller = SellerSerializers()
    buyers = ListBuyersSerializers(many=True, read_only=True)

    class Meta:
        model = Items

        fields = ['id', 'name', 'seller', 'price', 'image', 'description', 'buyers', 'has_been_sold', 'sold_to']

        extra_kwargs = {
            "id":{
                "read_only": True
            }
        }