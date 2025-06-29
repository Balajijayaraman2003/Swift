from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from . models import *
from . serializers import *
# Create your views here.

class FundViews(ModelViewSet):
    queryset = Fund.objects.all()
    serializer_class = Fund_Serial

class ExpenceViews(ModelViewSet):
    queryset = Expence.objects.all()
    serializer_class = Expence_Serial
    