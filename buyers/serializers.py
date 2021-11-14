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
    item = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Buyers
        fields = '__all__'

        extra_kwargs = {
            "id":{
                "read_only": True
            }
        }
