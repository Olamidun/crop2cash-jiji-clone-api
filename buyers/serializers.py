from .models import Buyers
from items.models import Items
from rest_framework import serializers


class ListBuyersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Buyers
        exclude = ['item']

        extra_kwargs = {
            "id":{
                "read_only": True
            }
        }


# Serializer that gets used when a seller chooses a buyer out of the interested buyers.
class CreateInterestedBuyerSerializer(serializers.Serializer):
    item_id = serializers.IntegerField(write_only=True)
    name = serializers.CharField()
    email = serializers.EmailField()
    location = serializers.CharField()

    def create(self, validated_data):
        item_id = validated_data.pop('item_id')
        print(type(item_id))
        item_data = Items.objects.get(id=item_id)
        buyer = Buyers.objects.filter(email=validated_data['email'])
        if buyer.exists():
            buyer.first().item.add(item_data)
            return validated_data
        else:
            buyer = Buyers.objects.create(**validated_data)
            print(buyer)
            buyer.item.add(item_data)
            return validated_data
