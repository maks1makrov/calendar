from django.contrib import auth
from django.contrib.auth import get_user_model, login
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import UserSerializer, LoginSerializer


User = get_user_model()

class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            if serializer.user is not None:
                token = Token.objects.create(user=serializer.user)
                send_mail('helo from cloud', f'{token.key}', 'maks1makrov@gmail.com', [serializer.data['email']],
                          fail_silently=False)
            return Response(f'{token.key}', status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)
        login(request, user)

        if user:
            token = Token.objects.get(user=user)
            serializer = UserSerializer(user)

            return Response(f'There is your token: {token.key}', status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)