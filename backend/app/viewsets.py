from rest_framework import viewsets 
from rest_framework.pagination import PageNumberPagination

from app.models import User, Message
from app.serializers import UserSerializer, MessageSerializer, ChatMessageSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = PageNumberPagination


class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = ChatMessageSerializer
    pagination_class = PageNumberPagination
