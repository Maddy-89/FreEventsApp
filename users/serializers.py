from rest_framework import serializers
from eventFinderApp.models import Event
from .models import CustomUser

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'location', 'start_time', 'end_time', 'categories', 'host']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']