from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import RegistrationSerializer, LoginSerializer

class RegistrationAPIView(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            return Response({
                'email': user.email,
                'token': user.auth_token.key
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
