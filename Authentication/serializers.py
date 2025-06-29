from rest_framework import serializers
from django.contrib.auth.models import User
from Authentication.models import *

class User_Serial(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'}, label="Confirm Password")


    class Meta:
        model = User
        fields = ["first_name","last_name","username","email","password","password2"]
        #extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password2": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.set_password(validated_data['password']) 
        user.save()
        return user



class Quardinator_Serial(serializers.ModelSerializer):
    user = User_Serial()  

    class Meta:
        model = Quardinators
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop('user')

        user_serializer = User_Serial(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        
        quardinator = Quardinators.objects.create(user=user, **validated_data)
        return quardinator

        
class Secretry_Serial(serializers.ModelSerializer):
    user= User_Serial()
    class Meta:
        model = Secretry
        fields = "__all__"
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = User_Serial(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        
        secretry = Secretry.objects.create(user=user,**validated_data)
        
        return secretry
    
class Tresurer_Serial(serializers.ModelSerializer):
    user= User_Serial()
    class Meta:
        model = Trusherer
        fields = "__all__"
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = User_Serial(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        
        trusherer = Trusherer.objects.create(user=user,**validated_data)
        
        return trusherer
    
class Swifters_Serial(serializers.ModelSerializer):
    user= User_Serial()
    class Meta:
        model = Swifters
        fields="__all__"
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = User_Serial(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        
        swifters = Swifters.objects.create(user=user,**validated_data)
        return swifters
    

class Students_Serial(serializers.ModelSerializer):
    user = User_Serial()
    class Meta:
        model = Students
        fields = "__all__"
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = User_Serial(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        
        student = Students.objects.create(user=user,**validated_data)
        return student
        