from rest_framework import serializers
from .models import *

class Event_Serial(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"