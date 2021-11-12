from rest_framework import serializers
from .models import Items
from seller.serializers import UserSerializers

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

    class Meta:
        model = Items

        fields = '__all__'

        extra_kwargs = {
            "id":{
                "read_only": True
            }
        }