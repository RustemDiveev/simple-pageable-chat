from rest_framework import serializers 

from app.models import User, Message


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = "__all__" 


class MessageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Message 
        fields = "__all__"


class ChatMessageSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Message
        fields = "__all__"

