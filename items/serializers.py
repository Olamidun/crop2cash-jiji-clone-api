from rest_framework import serializers
from .models import Items
from seller.serializers import UserSerializers
from buyers.serializers import ListBuyersSerializers

class CreateItemSerializer(serializers.ModelSerializer):
    seller = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Items
        fields = ['id', 'name', 'seller', 'price', 'image', 'description', 'has_been_sold']

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }


class ItemListSerializer(serializers.ModelSerializer):
    seller = UserSerializers()
    number_of_interested_buyers = serializers.SerializerMethodField('get_number_of_buyers')
    # buyers = ListBuyersSerializers(many=True, read_only=True)

    class Meta:
        model = Items

        fields = ['id', 'name', 'seller', 'price', 'image', 'description', 'number_of_interested_buyers', 'has_been_sold']
        # fields = ['buyers', 'seller']
        # depth = 1

        extra_kwargs = {
            "id":{
                "read_only": True
            }
        }

    def get_number_of_buyers(self, obj):
        buyer_count = obj.number_of_buyers()
        return buyer_count


class ItemDetailSerializer(serializers.ModelSerializer):
    seller = UserSerializers()
    buyers = ListBuyersSerializers(many=True, read_only=True)

    class Meta:
        model = Items

        fields = ['id', 'name', 'seller', 'price', 'image', 'description', 'buyers', 'has_been_sold']

        extra_kwargs = {
            "id":{
                "read_only": True
            }
        }