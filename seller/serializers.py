from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as JwtTokenObtainPairSerializer, PasswordField
from rest_framework_simplejwt.tokens import RefreshToken


UserModel = get_user_model()

# Override TokenObtainPairSerializer to use email as for authentication instead of username
class CustomTokenObtainPairSerializer(JwtTokenObtainPairSerializer):
    username_field = get_user_model().USERNAME_FIELD
#     print(username_field)


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

    def create(self, validated_data):
        seller = UserModel.objects.create_user(**validated_data)
        return seller




