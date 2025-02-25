
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User, Chat, Message
from .serializers import UserSerializer, ChatSerializer, MessageSerializer, UserRegistrationSerializer, UserLoginSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
class UserRegistrationView(APIView):
    """
    Регистрация нового пользователя.
    """
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Создаем пользователя
              # Генерируем токен
            return Response({'user-create'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    """
    Вход пользователя.
    """
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Проверяем данные
        user = serializer.validated_data  # Получаем пользователя из сериализатора
        token, _ = Token.objects.get_or_create(user=user)  # Генерируем/получаем токен
        return Response({'token': token.key}, status=status.HTTP_200_OK)
