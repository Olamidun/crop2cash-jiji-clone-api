from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenBlacklistSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegistrationSerializer, CustomTokenObtainPairSerializer

# Create your views here.

@api_view(['POST'])
def registration(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = serializer.data
        data['message'] = 'Your account has been created successfully'
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginWithEmailView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer