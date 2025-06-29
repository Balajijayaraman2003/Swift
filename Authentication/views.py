from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from Authentication.serializers import *
from Authentication.models import *
# Create your views here.

class QuardinatorsViews(ModelViewSet):
    queryset = Quardinators.objects.all()
    serializer_class = Quardinator_Serial
    
class SecretryViews(ModelViewSet):
    queryset = Secretry.objects.all()
    serializer_class = Secretry_Serial
    
class TrushererViews(ModelViewSet):
    queryset = Trusherer.objects.all()
    serializer_class = Tresurer_Serial
    
class SwiftersViews(ModelViewSet):
    queryset = Swifters.objects.all()
    serializer_class = Swifters_Serial

class StudentViews(ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = Students_Serial