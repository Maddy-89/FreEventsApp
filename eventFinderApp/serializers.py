from rest_framework import serializers
from .models import Event
from users.models import CustomUser

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'location', 'start_time', 'end_time', 'categories']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']