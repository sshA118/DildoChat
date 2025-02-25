from rest_framework import serializers
from .models import User, Chat, Message
from django.contrib.auth import  authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'avatar', 'bio']


class ChatSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Chat
        fields = ['id', 'name', 'type', 'participants']


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    chat = ChatSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'chat', 'content', 'timestamp']



class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    
class UserLoginSerializer(serializers.Serializer):
    """
    Сериализатор для входа пользователя.
    """
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")