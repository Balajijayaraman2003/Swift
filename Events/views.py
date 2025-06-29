from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
# Create your views here.

class EventViews(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = Event_Serial
    