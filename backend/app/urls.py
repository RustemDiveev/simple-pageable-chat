from django.urls import include, path 
from rest_framework import routers 

from app.viewsets import UserViewSet, MessageViewSet, ChatMessageViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'chatmessages', ChatMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]