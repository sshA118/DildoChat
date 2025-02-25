from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username


class Chat(models.Model):
    TYPE_CHOICES = (
        ('private', 'Private'),
        ('group', 'Group'),
    )

    name = models.CharField(max_length=255, null=True, blank=True)  # Для групповых чатов
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='private')
    participants = models.ManyToManyField(User, related_name='chats')

    def __str__(self):
        if self.type == 'private':
            return f"Private chat between {', '.join([user.username for user in self.participants.all()])}"
        return self.name or "Unnamed group"


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.sender.username}: {self.content[:20]}... ({self.timestamp})"