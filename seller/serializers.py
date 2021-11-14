from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as JwtTokenObtainPairSerializer

# leverage the function django has provided to access User model if it is a custom one
UserModel = get_user_model()

# Override TokenObtainPairSerializer to use email as for authentication instead of username
class CustomTokenObtainPairSerializer(JwtTokenObtainPairSerializer):
    username_field = get_user_model().USERNAME_FIELD


class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=15, write_only=True, min_length=10)

    class Meta:
        model = UserModel
        fields = ['id', 'first_name', 'last_name', 'email', 'state_of_residence', 'password']

        extra_kwargs = {
            'id': {
                'read_only': True
            }
        }

    # To do:
    #  - validate password to ensure its min_length doesn't exceed 10 and the max_lenght doesn't exceed 15

    def create(self, validated_data):
        seller = UserModel.objects.create_user(**validated_data)
        return seller


# Serializer to serializer information about seller to be displayed in some item's endpoint
class SellerSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'first_name', 'last_name', 'email', 'state_of_residence']





