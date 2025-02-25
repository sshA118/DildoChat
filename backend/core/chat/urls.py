from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ChatViewSet, MessageViewSet, UserRegistrationView, UserLoginView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'chats', ChatViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]