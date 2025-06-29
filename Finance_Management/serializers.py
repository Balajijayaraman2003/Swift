from rest_framework import serializers
from . models import *
class TotalFund_Serial(serializers.ModelSerializer):
    class Meta:
        model = TotalFund
        fields ="__all__"
        
class Fund_Serial(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields ="__all__"
    
            
class Expence_Serial(serializers.ModelSerializer):
    class Meta:
        model = Expence
        fields = "__all__"