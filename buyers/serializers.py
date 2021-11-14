from .models import Buyers
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


class CreateInterestedBuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyers
        fields = '__all__'

    # def create(self, validated_data):
    #     buyer = Buyers.objects.create(**validated_data)
    #     return buyer

        # extra_kwargs = {
        #     "id":{
        #         "read_only": True
        #     }
        # }
